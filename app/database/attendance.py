from datetime import datetime

from app.database.db import get_connection


def check_in(employee_id):
    today = datetime.now().strftime("%Y-%m-%d")
    now = datetime.now().strftime("%H:%M:%S")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id
        FROM attendance
        WHERE employee_id = ?
        AND date = ?
        """,
        (employee_id, today),
    )

    if cursor.fetchone():
        conn.close()
        return False

    cursor.execute(
        """
        INSERT INTO attendance
        (employee_id, date, check_in)
        VALUES (?, ?, ?)
        """,
        (employee_id, today, now),
    )

    conn.commit()
    conn.close()

    return True


def check_out(employee_id):
    today = datetime.now().strftime("%Y-%m-%d")
    now = datetime.now().strftime("%H:%M:%S")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE attendance
        SET check_out = ?
        WHERE employee_id = ?
        AND date = ?
        AND check_out IS NULL
        """,
        (now, employee_id, today),
    )

    updated = cursor.rowcount

    conn.commit()
    conn.close()

    return updated > 0


def get_today_attendance():
    today = datetime.now().strftime("%Y-%m-%d")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT employee_id, check_in, check_out
        FROM attendance
        WHERE date = ?
        ORDER BY check_in
        """,
        (today,),
    )

    data = cursor.fetchall()

    conn.close()

    return data