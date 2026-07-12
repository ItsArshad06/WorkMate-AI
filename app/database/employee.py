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
        (employee_id.upper(),),
    )

    employee = cursor.fetchone()

    conn.close()

    return employee


def employee_exists(employee_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT 1
        FROM employees
        WHERE employee_id = ?
        """,
        (employee_id.upper(),),
    )

    row = cursor.fetchone()

    conn.close()

    return row is not None


def get_all_employees():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT full_name, employee_id, department
        FROM employees
        ORDER BY full_name
        """
    )

    employees = cursor.fetchall()

    conn.close()

    return employees


def get_employee_count():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM employees"
    )

    count = cursor.fetchone()[0]

    conn.close()

    return count


def get_employee_details(employee_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT full_name,
               employee_id,
               department,
               phone
        FROM employees
        WHERE employee_id = ?
        """,
        (employee_id.upper(),),
    )

    employee = cursor.fetchone()

    conn.close()

    return employee