from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect as sa_inspect, text
from sqlalchemy.exc import OperationalError
import os
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from email_reset import send_reset_email
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'students.db')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_PATH}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'dev-secret-key'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

reset_tokens = {}  # In-memory storage for reset tokens (use database in production)

db = SQLAlchemy(app)


class Student(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	student_id = db.Column(db.String(50), unique=True, nullable=False)
	name = db.Column(db.String(120), nullable=False)
	age = db.Column(db.Integer, nullable=False)
	gender = db.Column(db.String(20), nullable=True)
	subject1 = db.Column(db.Integer, nullable=True)
	subject2 = db.Column(db.Integer, nullable=True)
	subject_cc = db.Column(db.Integer, nullable=True)
	subject_cd = db.Column(db.Integer, nullable=True)
	subject_ml = db.Column(db.Integer, nullable=True)
	subject_ai = db.Column(db.Integer, nullable=True)
	total = db.Column(db.Integer, nullable=True)
	percentage = db.Column(db.Float, nullable=True)
	status = db.Column(db.String(10), nullable=True)

	def __repr__(self):
		return f'<Student {self.id} {self.student_id} {self.name}>'


class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password_hash = db.Column(db.String(128), nullable=False)

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

	def __repr__(self):
		return f'<User {self.email}>'


@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))


with app.app_context():
	# Ensure database and tables exist when the app starts.
	db.create_all()

	# Create a default user if none exists
	if not User.query.first():
		default_user = User(email='admin@example.com')
		default_user.set_password('admin123')  # Change this password
		db.session.add(default_user)
		db.session.commit()

	# If the existing table is missing newly added columns, add them via ALTER TABLE
	try:
		inspector = sa_inspect(db.engine)
		if 'student' in inspector.get_table_names():
			cols = {c['name'] for c in inspector.get_columns('student')}
			needed = {
				'student_id': 'VARCHAR(50)',
				'gender': 'VARCHAR(20)',
				'subject1': 'INTEGER',
				'subject2': 'INTEGER',
				'subject_cc': 'INTEGER',
				'subject_cd': 'INTEGER',
				'subject_ml': 'INTEGER',
				'subject_ai': 'INTEGER',
				'total': 'INTEGER',
				'percentage': 'FLOAT',
				'status': 'VARCHAR(10)'
			}
			missing = [c for c in needed.keys() if c not in cols]
			for m in missing:
				try:
					db.session.execute(text(f'ALTER TABLE student ADD COLUMN {m} {needed[m]}'))
				except Exception:
					# ignore errors adding columns
					pass
			if missing:
				db.session.commit()
	except Exception:
		pass


@app.route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	if request.method == 'POST':
		email = request.form.get('email')
		password = request.form.get('password')
		confirm_password = request.form.get('confirm_password')
		if password != confirm_password:
			flash('Passwords do not match.', 'danger')
			return render_template('register.html')
		if User.query.filter_by(email=email).first():
			flash('Email already registered.', 'danger')
			return render_template('register.html')
		user = User(email=email)
		user.set_password(password)
		db.session.add(user)
		db.session.commit()
		flash('Account created successfully. Please log in.', 'success')
		return redirect(url_for('login'))
	return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	if request.method == 'POST':
		email = request.form.get('email')
		password = request.form.get('password')
		user = User.query.filter_by(email=email).first()
		if user and user.check_password(password):
			login_user(user)
			next_page = request.args.get('next')
			return redirect(next_page) if next_page else redirect(url_for('index'))
		flash('Invalid email or password.', 'danger')
	return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('login'))


@app.route('/forget_password', methods=['GET', 'POST'])
def forget_password():
	if request.method == 'POST':
		email = request.form.get('email')
		user = User.query.filter_by(email=email).first()
		if user:
			token = send_reset_email(email)
			if token:
				reset_tokens[token] = {'user_id': user.id, 'expires': time.time() + 3600}  # 1 hour
				flash('A reset link has been sent to your email.', 'info')
			else:
				flash('Failed to send reset email.', 'danger')
		else:
			flash('Email not found.', 'danger')
	return render_template('forget_password.html')


@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
	if token not in reset_tokens or time.time() > reset_tokens[token]['expires']:
		flash('Invalid or expired token.', 'danger')
		return redirect(url_for('login'))
	if request.method == 'POST':
		password = request.form.get('password')
		confirm_password = request.form.get('confirm_password')
		if password != confirm_password:
			flash('Passwords do not match.', 'danger')
			return render_template('reset_password.html')
		user = User.query.get(reset_tokens[token]['user_id'])
		user.set_password(password)
		db.session.commit()
		del reset_tokens[token]
		flash('Password reset successful. Please log in.', 'success')
		return redirect(url_for('login'))
	return render_template('reset_password.html')


@app.route('/')
@login_required
def index():
	students = Student.query.order_by(Student.id).all()
	return render_template('students.html', students=students)


@app.route('/add', methods=['GET', 'POST'])
@login_required
def add():
	if request.method == 'POST':
		student_id = request.form.get('student_id', '').strip()
		name = request.form.get('name', '').strip()
		age = request.form.get('age', '').strip()
		gender = request.form.get('gender', '').strip()
		# new subject fields
		sub_cc = request.form.get('subject_cc', '').strip()
		sub_cd = request.form.get('subject_cd', '').strip()
		sub_ml = request.form.get('subject_ml', '').strip()
		sub_ai = request.form.get('subject_ai', '').strip()

		if not student_id or not name or not age.isdigit():
			flash('Please provide a valid student id, name and numeric age.', 'danger')
			return redirect(url_for('add'))

		# collect provided subject marks (must supply at least 3 of the subject columns)
		marks = []
		for v in (sub_cc, sub_cd, sub_ml, sub_ai):
			if v and v.isdigit():
				marks.append(int(v))

		if len(marks) < 3:
			flash('Please provide marks for at least 3 subjects (CC, CD, ML, AI).', 'danger')
			return redirect(url_for('add'))

		total = sum(marks)
		percent = total / len(marks)
		status = 'PASS' if percent >= 40 else 'FAIL'

		student = Student(student_id=student_id, name=name, age=int(age), gender=gender,
				subject_cc=int(sub_cc) if sub_cc.isdigit() else None,
				subject_cd=int(sub_cd) if sub_cd.isdigit() else None,
				subject_ml=int(sub_ml) if sub_ml.isdigit() else None,
				subject_ai=int(sub_ai) if sub_ai.isdigit() else None,
				total=total, percentage=percent, status=status)
		db.session.add(student)
		try:
			db.session.commit()
		except OperationalError as e:
			db.session.rollback()
			if 'no column named' in str(e).lower():
				# backup old DB and recreate schema
				if os.path.exists(DB_PATH):
					try:
						os.replace(DB_PATH, DB_PATH + '.bak')
					except Exception:
						pass
					db.create_all()
					# retry insert
					db.session.add(student)
					db.session.commit()
			else:
				raise
		flash('Student added.', 'success')
		return redirect(url_for('index'))

	return render_template('form.html', action=url_for('add'), student=None)


@app.route('/edit/<student_id>', methods=['GET', 'POST'])
@login_required
def edit(student_id):
	student = Student.query.filter_by(student_id=student_id).first_or_404()
	if request.method == 'POST':
		student_id_val = request.form.get('student_id', '').strip()
		name = request.form.get('name', '').strip()
		age = request.form.get('age', '').strip()
		gender = request.form.get('gender', '').strip()
		sub_cc = request.form.get('subject_cc', '').strip()
		sub_cd = request.form.get('subject_cd', '').strip()
		sub_ml = request.form.get('subject_ml', '').strip()
		sub_ai = request.form.get('subject_ai', '').strip()

		if not student_id_val or not name or not age.isdigit():
			flash('Please provide a valid student id, name and numeric age.', 'danger')
			return redirect(url_for('edit', student_id=student_id))

		marks = []
		for v in (sub_cc, sub_cd, sub_ml, sub_ai):
			if v and v.isdigit():
				marks.append(int(v))

		if len(marks) < 3:
			flash('Please provide marks for at least 3 subjects (CC, CD, ML, AI).', 'danger')
			return redirect(url_for('edit', student_id=student_id))

		total = sum(marks)
		percent = total / len(marks)
		status = 'PASS' if percent >= 40 else 'FAIL'

		student.student_id = student_id_val
		student.name = name
		student.age = int(age)
		student.gender = gender
		student.subject_cc = int(sub_cc) if sub_cc.isdigit() else None
		student.subject_cd = int(sub_cd) if sub_cd.isdigit() else None
		student.subject_ml = int(sub_ml) if sub_ml.isdigit() else None
		student.subject_ai = int(sub_ai) if sub_ai.isdigit() else None
		student.total = total
		student.percentage = percent
		student.status = status
		try:
			db.session.commit()
		except OperationalError as e:
			db.session.rollback()
			if 'no column named' in str(e).lower():
				if os.path.exists(DB_PATH):
					try:
						os.replace(DB_PATH, DB_PATH + '.bak')
					except Exception:
						pass
					db.create_all()
					# re-fetch the student object and re-apply changes using new fields
					student = Student.query.filter_by(student_id=student_id_val).first_or_404()
					student.student_id = student_id_val
					student.name = name
					student.age = int(age)
					student.gender = gender
					student.subject_cc = int(sub_cc) if sub_cc.isdigit() else None
					student.subject_cd = int(sub_cd) if sub_cd.isdigit() else None
					student.subject_ml = int(sub_ml) if sub_ml.isdigit() else None
					student.subject_ai = int(sub_ai) if sub_ai.isdigit() else None
					student.total = total
					student.percentage = percent
					student.status = status
					db.session.commit()
			else:
				raise
		flash('Student updated.', 'success')
		return redirect(url_for('index'))

	return render_template('form.html', action=url_for('edit', student_id=student.student_id), student=student)


@app.route('/delete/<student_id>', methods=['POST'])
@login_required
def delete(student_id):
	student = Student.query.filter_by(student_id=student_id).first_or_404()
	db.session.delete(student)
	db.session.commit()
	flash('Student deleted.', 'success')
	return redirect(url_for('index'))


if __name__ == '__main__':
	app.run(debug=True)

