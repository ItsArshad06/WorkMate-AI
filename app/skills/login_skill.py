from app.ai.session import session
from app.database.employee import get_employee


class LoginSkill:

    def execute(self, telegram_user_id, employee_id):

        employee = get_employee(employee_id)

        if not employee:
            return (
                "❌ Employee ID not found.\n"
                "Please enter a valid Employee ID."
            )

        session.login(
            telegram_user_id=telegram_user_id,
            employee_id=employee["employee_id"],
            role="EMPLOYEE",
            employee_name=employee["full_name"],
            department=employee["department"],
        )

        return (
            f"✅ Welcome back, {employee['full_name']}!\n\n"
            f"🏢 Department: {employee['department']}\n\n"
            "You can now talk to me naturally."
        )


login_skill = LoginSkill()