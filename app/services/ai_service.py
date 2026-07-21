from app.services.intent_detector import detect_intent

from app.utils.permissions import has_permission

from app.intelligence.attendance_ai import attendance_summary
from app.intelligence.leave_ai import leave_summary
from app.intelligence.employee_ai import employee_summary
from app.intelligence.hr_ai import (
    employee_count,
    pending_leave_report,
    missing_attendance_report,
    hr_dashboard,
)


def ask_ai(employee_id: str, telegram_user_id: int, message: str):

    intent = detect_intent(message)

    # ==========================================
    # Permission Check
    # ==========================================

    if not has_permission(telegram_user_id, intent):

        return (
            "🔒 This feature is available only to HR users."
        )

    # ==========================================
    # Employee Dashboard
    # ==========================================

    if intent == "dashboard":

        return (
            employee_summary(employee_id)
            + "\n\n"
            + attendance_summary(employee_id)
            + "\n\n"
            + leave_summary(employee_id)
        )

    # ==========================================
    # Employee Features
    # ==========================================

    elif intent == "attendance":

        return attendance_summary(employee_id)

    elif intent == "leave":

        return leave_summary(employee_id)

    elif intent == "profile":

        return employee_summary(employee_id)

    # ==========================================
    # HR Intelligence
    # ==========================================

    elif intent == "employee_count":

        return employee_count()

    elif intent == "pending_leaves":

        return pending_leave_report()

    elif intent == "missing_attendance":

        return missing_attendance_report()

    elif intent == "hr_dashboard":

        return hr_dashboard()

    # ==========================================
    # Unknown Intent
    # ==========================================

    return (
        "🤖 I don't understand that yet.\n\n"
        "Try asking about:\n"
        "• Attendance\n"
        "• Leave\n"
        "• Profile\n"
        "• Dashboard"
    )