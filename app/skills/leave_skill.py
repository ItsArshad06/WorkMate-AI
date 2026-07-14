from app.ai.conversation import conversation
from app.ai.session import session
from app.database.leave import create_leave


class LeaveSkill:

    def execute(self, user_id, message):

        employee_id = session.employee_id(user_id)

        if employee_id is None:
            return (
                "🔐 Please login first.\n"
                "Enter your Employee ID."
            )

        current = conversation.get(user_id)

        if not current:
            conversation.start(user_id, "APPLY_LEAVE")
            current = conversation.get(user_id)

        step = current["step"]

        # -----------------------------
        # Start Leave Flow
        # -----------------------------
        if step == "START":

            conversation.save_data(
                user_id,
                "employee_id",
                employee_id,
            )

            conversation.update_step(
                user_id,
                "WAITING_START_DATE",
            )

            return "📅 Enter Start Date (YYYY-MM-DD)"

        # -----------------------------
        # Start Date
        # -----------------------------
        elif step == "WAITING_START_DATE":

            conversation.save_data(
                user_id,
                "start_date",
                message,
            )

            conversation.update_step(
                user_id,
                "WAITING_END_DATE",
            )

            return "📅 Enter End Date (YYYY-MM-DD)"

        # -----------------------------
        # End Date
        # -----------------------------
        elif step == "WAITING_END_DATE":

            conversation.save_data(
                user_id,
                "end_date",
                message,
            )

            conversation.update_step(
                user_id,
                "WAITING_REASON",
            )

            return "📝 Enter Leave Reason"

        # -----------------------------
        # Reason
        # -----------------------------
        elif step == "WAITING_REASON":

            conversation.save_data(
                user_id,
                "reason",
                message,
            )

            data = conversation.get(user_id)["data"]

            create_leave(
                data["employee_id"],
                data["start_date"],
                data["end_date"],
                data["reason"],
            )

            conversation.clear(user_id)

            return (
                "✅ Leave Applied Successfully!\n\n"
                f"👤 Employee: {data['employee_id']}\n"
                f"📅 From: {data['start_date']}\n"
                f"📅 To: {data['end_date']}\n"
                f"📝 Reason: {data['reason']}"
            )

        return "❌ Something went wrong."


leave_skill = LeaveSkill()