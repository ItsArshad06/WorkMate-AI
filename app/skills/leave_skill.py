from app.ai.conversation import conversation
from app.database.leave import create_leave


class LeaveSkill:

    def execute(self, user_id, message):

        session = conversation.get(user_id)

        if not session:
            conversation.start(user_id, "APPLY_LEAVE")
            return "🆔 Please enter your Employee ID."

        step = session["step"]

        if step == "START":

            conversation.update_step(
                user_id,
                "WAITING_EMPLOYEE_ID",
            )

            return "🆔 Please enter your Employee ID."

        elif step == "WAITING_EMPLOYEE_ID":

            conversation.save_data(
                user_id,
                "employee_id",
                message.upper(),
            )

            conversation.update_step(
                user_id,
                "WAITING_START_DATE",
            )

            return "📅 Enter Start Date (YYYY-MM-DD)"

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