from app.database.db import get_connection


def save_employee(full_name, employee_id, department, phone):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO employees
        (full_name, employee_id, department, phone)
        VALUES (?, ?, ?, ?)
        """,
        (full_name, employee_id, department, phone),
    )

    conn.commit()
    conn.close()