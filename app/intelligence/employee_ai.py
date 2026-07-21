
from app.database.employee import get_employee


def employee_summary(employee_id):

    employee = get_employee(employee_id)

    if employee is None:
        return "Employee not found."

    return (
        f"👤 Employee Profile\n\n"
        f"Name : {employee['full_name']}\n"
        f"Employee ID : {employee['employee_id']}\n"
        f"Department : {employee['department']}\n"
        f"Role : {employee['role']}\n"
        f"Email : {employee['email']}\n"
        f"Phone : {employee['phone']}\n"
        f"Joining Date : {employee['joining_date']}\n"
        f"Status : {employee['status']}"
    )