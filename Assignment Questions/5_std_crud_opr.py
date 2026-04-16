from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect as sa_inspect, text
from sqlalchemy.exc import OperationalError
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'students.db')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_PATH}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'dev-secret-key'

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


with app.app_context():
	# Ensure database and tables exist when the app starts.
	db.create_all()

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


@app.route('/')
def index():
	students = Student.query.order_by(Student.id).all()
	return render_template('students.html', students=students)


@app.route('/add', methods=['GET', 'POST'])
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
def delete(student_id):
	student = Student.query.filter_by(student_id=student_id).first_or_404()
	db.session.delete(student)
	db.session.commit()
	flash('Student deleted.', 'success')
	return redirect(url_for('index'))


if __name__ == '__main__':
	app.run(debug=True)

