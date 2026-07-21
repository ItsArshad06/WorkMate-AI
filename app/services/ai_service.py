from app.services.intent_detector import detect_intent

from app.intelligence.attendance_ai import attendance_summary
from app.intelligence.leave_ai import leave_summary
from app.intelligence.employee_ai import employee_summary


def ask_ai(employee_id: str, message: str):

    intent = detect_intent(message)


    # ========================================
    # Dashboard
    # ========================================

    if intent == "dashboard":

        attendance = attendance_summary(employee_id)
        leave = leave_summary(employee_id)
        profile = employee_summary(employee_id)

        return (
            f"{profile}\n\n"
            f"{attendance}\n\n"
            f"{leave}"
        )


    # ========================================
    # Attendance
    # ========================================

    elif intent == "attendance":

        return attendance_summary(employee_id)


    # ========================================
    # Leave
    # ========================================

    elif intent == "leave":

        return leave_summary(employee_id)


    # ========================================
    # Profile
    # ========================================

    elif intent == "profile":

        return employee_summary(employee_id)


    # ========================================
    # Unknown
    # ========================================

    return (
        "🤖 I'm still learning.\n\n"
        "You can ask me:\n\n"
        "• Show my dashboard\n"
        "• Show my attendance\n"
        "• Show my leave summary\n"
        "• Show my profile"
    )