from app.database.db import get_connection



def save_employee(
    full_name,
    employee_id,
    email,
    phone,
    department,
    role,
    joining_date,
    status
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO employees
        (
            full_name,
            employee_id,
            email,
            phone,
            department,
            role,
            joining_date,
            status
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            full_name,
            employee_id.upper(),
            email,
            phone,
            department,
            role,
            joining_date,
            status
        )
    )

    conn.commit()
    conn.close()



def get_employee(employee_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            full_name,
            employee_id,
            email,
            phone,
            department,
            role,
            joining_date,
            status
        FROM employees
        WHERE employee_id = ?
        """,
        (employee_id.upper(),)
    )

    employee = cursor.fetchone()

    conn.close()

    return employee



def get_employee_details(employee_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            id,
            full_name,
            employee_id,
            email,
            phone,
            department,
            role,
            joining_date,
            status
        FROM employees
        WHERE employee_id = ?
        """,
        (employee_id.upper(),)
    )

    employee = cursor.fetchone()

    conn.close()

    return employee



def get_all_employees():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            id,
            full_name,
            employee_id,
            email,
            phone,
            department,
            role,
            joining_date,
            status
        FROM employees
        ORDER BY full_name
        """
    )

    employees = cursor.fetchall()

    conn.close()

    return employees



def employee_exists(employee_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT 1
        FROM employees
        WHERE employee_id = ?
        """,
        (employee_id.upper(),)
    )

    result = cursor.fetchone()

    conn.close()

    return result is not None



def get_employee_count():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM employees"
    )

    count = cursor.fetchone()[0]

    conn.close()

    return count



def delete_employee(employee_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM employees
        WHERE employee_id = ?
        """,
        (employee_id.upper(),)
    )

    conn.commit()

    conn.close()