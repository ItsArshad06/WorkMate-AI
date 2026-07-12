"""
WorkMate AI - Session Service
"""

from app.database.session import (
    save_session,
    get_session,
    delete_session,
    update_last_active,
)


class SessionManager:

    def login(
        self,
        telegram_user_id,
        employee_id,
        role,
        employee_name,
        department,
    ):
        save_session(
            telegram_user_id,
            employee_id,
            role,
            employee_name,
            department,
        )

    def logout(self, telegram_user_id):
        delete_session(telegram_user_id)

    def get(self, telegram_user_id):
        session = get_session(telegram_user_id)

        if session:
            update_last_active(telegram_user_id)

        return session

    def is_logged_in(self, telegram_user_id):
        return self.get(telegram_user_id) is not None

    def employee_id(self, telegram_user_id):
        session = self.get(telegram_user_id)

        if session:
            return session["employee_id"]

        return None

    def role(self, telegram_user_id):
        session = self.get(telegram_user_id)

        if session:
            return session["role"]

        return None


session = SessionManager()