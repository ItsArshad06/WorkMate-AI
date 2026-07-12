from app.database.employee import get_employee_details


class ProfileSkill:

    def execute(self, user_id, message):

        # Temporary
        employee_id = "EMP001"

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