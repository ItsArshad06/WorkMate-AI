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


def get_employee(employee_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT full_name, employee_id, department, phone
        FROM employees
        WHERE employee_id = ?
        """,
        (employee_id,),
    )

    employee = cursor.fetchone()

    conn.close()

    return employee


def employee_exists(employee_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT 1 FROM employees WHERE employee_id = ?",
        (employee_id,),
    )

    row = cursor.fetchone()
    print("DEBUG:", employee_id, row)

    exists = row is not None

    conn.close()

    return exists