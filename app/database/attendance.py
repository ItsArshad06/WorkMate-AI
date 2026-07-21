from datetime import datetime

from app.database.db import get_connection


def check_in(employee_id):

    today = datetime.now().strftime("%Y-%m-%d")
    now = datetime.now().strftime("%H:%M:%S")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM attendance
        WHERE employee_id = ?
        AND date = ?
        """,
        (employee_id, today),
    )

    row = cursor.fetchone()

    if row:
        conn.close()
        return "ALREADY_CHECKED_IN"

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

    return "SUCCESS"



def check_out(employee_id):

    today = datetime.now().strftime("%Y-%m-%d")
    now = datetime.now().strftime("%H:%M:%S")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT check_out
        FROM attendance
        WHERE employee_id = ?
        AND date = ?
        """,
        (employee_id, today),
    )

    row = cursor.fetchone()

    if row is None:
        conn.close()
        return "NOT_CHECKED_IN"

    if row["check_out"] is not None:
        conn.close()
        return "ALREADY_CHECKED_OUT"


    cursor.execute(
        """
        UPDATE attendance
        SET check_out = ?
        WHERE employee_id = ?
        AND date = ?
        """,
        (now, employee_id, today),
    )

    conn.commit()
    conn.close()

    return "SUCCESS"



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



def get_employee_attendance(employee_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            id,
            employee_id,
            date,
            check_in,
            check_out
        FROM attendance
        WHERE employee_id = ?
        ORDER BY date DESC
        """,
        (employee_id.upper(),)
    )

    attendance = cursor.fetchall()

    conn.close()

    return attendance



def get_today_attendance_count():

    today = datetime.now().strftime("%Y-%m-%d")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM attendance
        WHERE date = ?
        """,
        (today,),
    )

    count = cursor.fetchone()[0]

    conn.close()

    return count