from app.ai.session import session
from app.database.attendance import check_in, check_out


class AttendanceSkill:

    def execute(self, user_id, message):

        employee_id = session.employee_id(user_id)

        if employee_id is None:
            return (
                "🔐 Please login first.\n"
                "Enter your Employee ID."
            )

        text = message.lower().strip()

        checkin_keywords = [
            "check in",
            "checkin",
            "check me in",
            "i'm here",
            "im here",
            "present",
            "arrived",
        ]

        checkout_keywords = [
            "check out",
            "checkout",
            "check me out",
            "going home",
            "leaving",
            "bye",
        ]

        if any(keyword in text for keyword in checkin_keywords):

            result = check_in(employee_id)

            if result == "SUCCESS":
                return (
                    "✅ Check-in successful!\n\n"
                    f"👤 Employee: {employee_id}"
                )

            if result == "ALREADY_CHECKED_IN":
                return "⚠️ You have already checked in today."

        if any(keyword in text for keyword in checkout_keywords):

            result = check_out(employee_id)

            if result == "SUCCESS":
                return (
                    "👋 Check-out successful!\n"
                    "Have a great day!"
                )

            if result == "ALREADY_CHECKED_OUT":
                return "⚠️ You have already checked out today."

            if result == "NOT_CHECKED_IN":
                return "⚠️ You haven't checked in today."

        return "❌ I couldn't understand your attendance request."


attendance_skill = AttendanceSkill()