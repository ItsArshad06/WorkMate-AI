from app.database.attendance import check_in, check_out


class AttendanceSkill:

    def execute(self, user_id, message):

        text = message.lower().strip()

        employee_id = "EMP001"

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

            return "⚠️ You haven't checked in today."

        return "❌ I couldn't understand your attendance request."


attendance_skill = AttendanceSkill()