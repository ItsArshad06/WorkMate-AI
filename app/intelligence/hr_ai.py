from app.database.employee import get_all_employees
from app.database.leave import (
    get_all_leaves,
    get_leave_statistics,
)
from app.database.attendance import (
    get_today_attendance,
    get_today_attendance_count,
)


# ==========================================
# Employee Count
# ==========================================

def employee_count():

    employees = get_all_employees()

    return (
        f"👥 Employee Overview\n\n"
        f"Total Employees: {len(employees)}"
    )


# ==========================================
# Pending Leave Report
# ==========================================

def pending_leave_report():

    leaves = get_all_leaves()

    pending = [
        leave
        for leave in leaves
        if leave["status"].lower() == "pending"
    ]

    if not pending:
        return "✅ No pending leave requests."

    message = (
        "📝 Pending Leave Requests\n\n"
        f"Total Pending: {len(pending)}\n\n"
    )

    for leave in pending:

        message += (
            f"👤 Employee : {leave['employee_id']}\n"
            f"📅 From : {leave['start_date']}\n"
            f"📅 To : {leave['end_date']}\n"
            f"📌 Status : {leave['status']}\n\n"
        )

    return message


# ==========================================
# Missing Attendance
# ==========================================

def missing_attendance_report():

    employees = get_all_employees()
    attendance = get_today_attendance()

    present_ids = {
        record["employee_id"].upper()
        for record in attendance
    }

    missing = []

    for employee in employees:

        if employee["employee_id"].upper() not in present_ids:
            missing.append(employee)

    if not missing:
        return "✅ Everyone has checked in today."

    message = "⚠️ Employees Without Attendance Today\n\n"

    for employee in missing:

        message += (
            f"• {employee['full_name']} "
            f"({employee['employee_id']})\n"
        )

    return message


# ==========================================
# HR Dashboard
# ==========================================

def hr_dashboard():

    employees = get_all_employees()

    total_employees = len(employees)

    present_today = get_today_attendance_count()

    absent_today = total_employees - present_today

    leave_stats = get_leave_statistics()

    return (
        "📊 HR Dashboard\n\n"
        f"👥 Total Employees : {total_employees}\n"
        f"🟢 Present Today : {present_today}\n"
        f"🔴 Absent Today : {absent_today}\n\n"
        f"📝 Pending Leaves : {leave_stats['Pending']}\n"
        f"✅ Approved Leaves : {leave_stats['Approved']}\n"
        f"❌ Rejected Leaves : {leave_stats['Rejected']}"
    )