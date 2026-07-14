from app.ai.session import session
from app.database.employee import get_employee_details


class ProfileSkill:

    def execute(self, user_id, message):

        employee_id = session.employee_id(user_id)

        if employee_id is None:
            return (
                "🔐 Please login first.\n"
                "Enter your Employee ID."
            )

        employee = get_employee_details(employee_id)

        if employee is None:
            return "❌ Employee profile not found."

        return (
            "👤 Employee Profile\n"
            "━━━━━━━━━━━━━━━━━━\n\n"
            f"👤 Name: {employee['full_name']}\n"
            f"🆔 Employee ID: {employee['employee_id']}\n"
            f"🏢 Department: {employee['department']}\n"
            f"📱 Phone: {employee['phone']}"
        )


profile_skill = ProfileSkill()