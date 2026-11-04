
from flask import Flask, render_template
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "students.db"

app = Flask(__name__)


def get_db():
    conn = sqlite3.connect(DB_PATH, timeout=10)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with get_db() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                idno TEXT NOT NULL UNIQUE,
                lastname TEXT NOT NULL,
                firstname TEXT NOT NULL,
                course TEXT NOT NULL,
                level INTEGER NOT NULL
            )
        """)

        conn.executemany("""
            INSERT OR IGNORE INTO students
            (idno, lastname, firstname, course, level)
            VALUES (?, ?, ?, ?, ?)
        """, [
            ("1000", "hotel", "india", "bscs", 3),
            ("1001", "juliet", "kilo", "bsit", 4),
            ("1002", "hello", "world", "bscs", 2),
            ("1003", "tango", "whiskey", "bscs", 2),
            ("1004", "durano", "dennis", "bscs", 2),
        ])


@app.route("/")
def student_list():
    with get_db() as conn:
        students = conn.execute("""
            SELECT id, idno, lastname, firstname, course, level
            FROM students
            ORDER BY id
        """).fetchall()

    return render_template("index.html", students=students)


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=False)
