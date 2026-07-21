from app.database.attendance import get_employee_attendance


def attendance_summary(employee_id):

    attendance = get_employee_attendance(employee_id)

    if not attendance:
        return "You don't have any attendance records."

    total_days = len(attendance)

    latest = attendance[0]

    check_in = latest["check_in"] or "-"
    check_out = latest["check_out"] or "-"

    return (
        f"📅 Attendance Summary\n\n"
        f"Total Attendance Days : {total_days}\n"
        f"Latest Check In : {check_in}\n"
        f"Latest Check Out : {check_out}"
    )