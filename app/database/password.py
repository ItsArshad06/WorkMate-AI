from app.database.db import get_connection
from app.security.security import hash_password


def set_password(employee_id: str, password: str):

    conn = get_connection()
    cursor = conn.cursor()

    password_hash = hash_password(password)

    cursor.execute(
        """
        UPDATE employees
        SET password_hash = ?
        WHERE employee_id = ?
        """,
        (
            password_hash,
            employee_id.upper()
        )
    )

    conn.commit()
    conn.close()


def get_password_hash(employee_id: str):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT password_hash
        FROM employees
        WHERE employee_id = ?
        """,
        (employee_id.upper(),)
    )

    row = cursor.fetchone()

    conn.close()

    if row is None:
        return None

    return row["password_hash"]