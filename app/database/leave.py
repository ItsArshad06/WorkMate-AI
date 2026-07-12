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


def get_pending_leaves():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, employee_id, start_date, end_date, reason
        FROM leaves
        WHERE status='Pending'
        ORDER BY id
        """
    )

    data = cursor.fetchall()

    conn.close()

    return data


def approve_leave(leave_id):
    update_leave_status(leave_id, "Approved")


def reject_leave(leave_id):
    update_leave_status(leave_id, "Rejected")


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


def get_pending_leave_count():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM leaves
        WHERE status='Pending'
        """
    )

    count = cursor.fetchone()[0]

    conn.close()

    return count


def get_approved_leave_count():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM leaves
        WHERE status='Approved'
        """
    )

    count = cursor.fetchone()[0]

    conn.close()

    return count


def get_rejected_leave_count():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM leaves
        WHERE status='Rejected'
        """
    )

    count = cursor.fetchone()[0]

    conn.close()

    return count