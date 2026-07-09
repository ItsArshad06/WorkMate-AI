from app.database.db import get_connection


def create_leave(employee_id, start_date, end_date, reason):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS leaves (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id TEXT,
            start_date TEXT,
            end_date TEXT,
            reason TEXT,
            status TEXT
        )
        """
    )

    cursor.execute(
        """
        INSERT INTO leaves
        (employee_id, start_date, end_date, reason, status)
        VALUES (?, ?, ?, ?, ?)
        """,
        (employee_id, start_date, end_date, reason, "Pending"),
    )

    conn.commit()
    conn.close()


def get_all_leaves():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, employee_id, start_date, end_date, reason, status
        FROM leaves
        ORDER BY id DESC
        """
    )

    leaves = cursor.fetchall()

    conn.close()

    return leaves


def update_leave_status(leave_id, status):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE leaves
        SET status = ?
        WHERE id = ?
        """,
        (status, leave_id),
    )

    conn.commit()
    conn.close()