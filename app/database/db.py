import sqlite3
from pathlib import Path

DB_PATH = Path("data/workmate.db")


def get_connection():
    DB_PATH.parent.mkdir(exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()

    # Employees
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        employee_id TEXT UNIQUE NOT NULL,
        department TEXT NOT NULL,
        phone TEXT NOT NULL
    )
    """)

    # Leaves
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS leaves(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        employee_id TEXT NOT NULL,
        start_date TEXT NOT NULL,
        end_date TEXT NOT NULL,
        reason TEXT NOT NULL,
        status TEXT NOT NULL
    )
    """)

    # Attendance
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS attendance(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        employee_id TEXT NOT NULL,
        date TEXT NOT NULL,
        check_in TEXT,
        check_out TEXT
    )
    """)

    # User Sessions
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_sessions(
        telegram_user_id INTEGER PRIMARY KEY,
        employee_id TEXT NOT NULL,
        role TEXT NOT NULL,
        employee_name TEXT NOT NULL,
        department TEXT NOT NULL,
        login_time TEXT NOT NULL,
        last_active TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()

    print("✅ Database initialized.")