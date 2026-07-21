from app.database.employee import get_employee
from app.database.leave import get_employee_leave_summary
from app.database.attendance import get_employee_attendance

from app.services.intent_detector import detect_intent


def ask_ai(employee_id: str, message: str):

    intent = detect_intent(message)

    employee = get_employee(employee_id)

    if employee is None:
        return "I couldn't find your employee record."

    # =========================================
    # DASHBOARD
    # =========================================

    if intent == "dashboard":

        summary = get_employee_leave_summary(employee_id)
        attendance = get_employee_attendance(employee_id)

        checkin = "-"
        checkout = "-"

        if attendance:
            latest = attendance[0]
            checkin = latest["check_in"] or "-"
            checkout = latest["check_out"] or "-"

        return (
            f"👤 Employee Dashboard\n\n"
            f"Name: {employee['full_name']}\n"
            f"Department: {employee['department']}\n\n"
            f"📅 Attendance\n"
            f"Check In : {checkin}\n"
            f"Check Out: {checkout}\n\n"
            f"📝 Leave Summary\n"
            f"Pending : {summary['Pending']}\n"
            f"Approved: {summary['Approved']}\n"
            f"Rejected: {summary['Rejected']}"
        )

    # =========================================
    # ATTENDANCE
    # =========================================

    elif intent == "attendance":

        attendance = get_employee_attendance(employee_id)

        if attendance:

            latest = attendance[0]

            return (
                f"📅 Latest Attendance\n\n"
                f"Date : {latest['date']}\n"
                f"Check In : {latest['check_in']}\n"
                f"Check Out: {latest['check_out'] or 'Not Checked Out'}"
            )

        return "You don't have any attendance records."

    # =========================================
    # LEAVE
    # =========================================

    elif intent == "leave":

        summary = get_employee_leave_summary(employee_id)

        return (
            f"📄 Leave Summary\n\n"
            f"Pending : {summary['Pending']}\n"
            f"Approved: {summary['Approved']}\n"
            f"Rejected: {summary['Rejected']}"
        )

    # =========================================
    # PROFILE
    # =========================================

    elif intent == "profile":

        return (
            f"👤 Employee Profile\n\n"
            f"Name : {employee['full_name']}\n"
            f"Employee ID : {employee['employee_id']}\n"
            f"Department : {employee['department']}\n"
            f"Phone : {employee['phone']}"
        )

    # =========================================
    # UNKNOWN
    # =========================================

    return (
        "🤖 I couldn't understand that yet.\n\n"
        "You can ask me things like:\n\n"
        "• Show my dashboard\n"
        "• Show my attendance\n"
        "• Show my profile\n"
        "• How many leaves do I have?"
    )