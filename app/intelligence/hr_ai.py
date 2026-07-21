from app.database.employee import get_all_employees
from app.database.leave import get_all_leaves
from app.database.attendance import get_today_attendance


def employee_count():

    employees = get_all_employees()

    return (
        f"👥 Employee Overview\n\n"
        f"Total Employees: {len(employees)}"
    )


def pending_leave_report():

    leaves = get_all_leaves()

    pending = [
        leave for leave in leaves
        if leave["status"].lower() == "pending"
    ]

    if not pending:
        return "✅ No pending leave requests."


    message = (
        f"📝 Pending Leave Requests\n\n"
        f"Total Pending: {len(pending)}\n\n"
    )


    for leave in pending:
        message += (
            f"👤 Employee: {leave['employee_id']}\n"
            f"📅 From: {leave['start_date']}\n"
            f"📅 To: {leave['end_date']}\n\n"
        )

    return message



def missing_attendance_report():

    employees = get_all_employees()
    attendance = get_today_attendance()


    present_ids = [
        record["employee_id"].upper()
        for record in attendance
    ]


    missing = [
        employee
        for employee in employees
        if employee["employee_id"].upper()
        not in present_ids
    ]


    if not missing:
        return "✅ Everyone has checked in today."


    message = (
        "⚠️ Employees Without Attendance Today\n\n"
    )


    for employee in missing:

        message += (
            f"• {employee['full_name']} "
            f"({employee['employee_id']})\n"
        )


    return message