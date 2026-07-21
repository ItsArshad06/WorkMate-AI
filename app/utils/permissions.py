from app.database.session import get_session


HR_INTENTS = {
    "employee_count",
    "pending_leaves",
    "missing_attendance",
    "hr_dashboard",
}


def is_hr_user(telegram_user_id):

    session = get_session(telegram_user_id)

    if session is None:
        return False

    return session["role"].lower() == "hr"


def has_permission(telegram_user_id, intent):

    if intent in HR_INTENTS:
        return is_hr_user(telegram_user_id)

    return True