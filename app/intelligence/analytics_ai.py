from app.database.attendance import get_all_attendance
from app.database.employee import (
    get_employee_count,
    get_all_employees,
)

from app.database.attendance import (
    get_present_count,
    get_absent_count,
)

from app.database.leave import (
    get_pending_leave_count,
    get_approved_leave_count,
    get_rejected_leave_count,
)


def attendance_percentage():

    total = get_employee_count()

    if total == 0:
        return 0

    present = get_present_count()

    return round((present / total) * 100, 2)


def leave_statistics():

    return {
        "pending": get_pending_leave_count(),
        "approved": get_approved_leave_count(),
        "rejected": get_rejected_leave_count(),
    }


def company_statistics():

    return {
        "employees": get_employee_count(),
        "present": get_present_count(),
        "absent": get_absent_count(),
        "attendance_percentage": attendance_percentage(),
        "leave": leave_statistics(),
    }


def department_distribution():

    employees = get_all_employees()

    departments = {}

    for employee in employees:

        department = employee["department"]

        departments[department] = (
            departments.get(department, 0) + 1
        )

    return departments
def department_summary():

    departments = department_distribution()

    if not departments:
        return (
            "🏢 Department Summary\n\n"
            "No employees found."
        )

    report = "🏢 Department Summary\n\n"

    total = sum(departments.values())

    for department, count in sorted(departments.items()):

        percentage = round((count / total) * 100, 1)

        report += (
            f"• {department}: "
            f"{count} employee(s) "
            f"({percentage}%)\n"
        )

    report += f"\nTotal Employees: {total}"

    return report
from app.database.attendance import get_all_attendance


def perfect_attendance():

    employees = get_all_employees()
    attendance = get_all_attendance()

    attendance_count = {}

    for row in attendance:
        emp_id = row["employee_id"]
        attendance_count[emp_id] = attendance_count.get(emp_id, 0) + 1

    if not employees:
        return "🏆 Perfect Attendance\n\nNo employees found."

    highest = max(attendance_count.values(), default=0)

    report = "🏆 Perfect Attendance\n\n"

    total = 0
    
    for employee in employees:

        emp_id = employee["employee_id"]

        if attendance_count.get(emp_id, 0) == highest and highest > 0:

            total += 1

            report += (
                f"• {employee['full_name']} "
                f"({emp_id})\n"
            )
    
    report += f"\nTotal: {total} Employee(s)"

    return report
def frequently_absent():

    employees = get_all_employees()

    attendance = get_all_attendance()

    attendance_count = {}

    for row in attendance:

        emp_id = row["employee_id"]

        attendance_count[emp_id] = attendance_count.get(emp_id, 0) + 1

    if not employees:

        return (
            "⚠ Frequently Absent Employees\n\n"
            "No employees found."
        )

    report = "⚠ Frequently Absent Employees\n\n"

    found = False

    highest = max(attendance_count.values(), default=0)

    for employee in employees:

        emp_id = employee["employee_id"]

        attended = attendance_count.get(emp_id, 0)

        absent = highest - attended

        if absent > 0:

            found = True

            report += (
                f"• {employee['full_name']} "
                f"({emp_id})\n"
                f"  Missed: {absent} day(s)\n\n"
            )

    if not found:

        report += "🎉 No employees have significant absences."

    return report
def executive_dashboard():

    report = (
        "📊 Executive Dashboard\n\n"
    )

    stats = company_statistics()

    report += (
        f"👥 Employees : {stats['employees']}\n"
        f"🟢 Present : {stats['present']}\n"
        f"🔴 Absent : {stats['absent']}\n"
        f"📈 Attendance : {stats['attendance_percentage']}%\n\n"
    )

    leave = stats["leave"]

    report += (
        "📝 Leave Summary\n"
        f"Pending : {leave['pending']}\n"
        f"Approved : {leave['approved']}\n"
        f"Rejected : {leave['rejected']}\n\n"
    )

    report += department_summary()

    report += "\n\n"

    report += perfect_attendance()

    report += "\n\n"

    report += frequently_absent()

    return report