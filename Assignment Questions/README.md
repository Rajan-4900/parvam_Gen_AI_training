# Student CRUD (Flask)

Simple Flask app demonstrating CRUD operations for students using SQLite and SQLAlchemy.

Setup (Windows PowerShell):

```powershell
python -m pip install -r requirements.txt
python "5_std_crud_opr.py"
```

Then open http://127.0.0.1:5000/ in your browser.

Notes:
- The app creates `students.db` in the same folder on first run.
- For production use, change the `SECRET_KEY` and disable `debug`.
