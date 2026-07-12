import re

from app.database.leave import (
    get_pending_leaves,
    approve_leave,
    reject_leave,
)
from app.utils.auth import is_hr


class HRLeaveSkill:

    def execute(self, user_id, message):

        # Temporary until Session Integration (Pack 8)
        employee_id = "EMP001"

        if not is_hr(employee_id):
            return "❌ Only HR can perform this action."

        text = message.lower().strip()

        # -------------------------
        # Show Pending Leaves
        # -------------------------
        if (
            "pending" in text
            or "show pending" in text
            or "pending leaves" in text
        ):

            leaves = get_pending_leaves()

            if not leaves:
                return "✅ There are no pending leave requests."

            response = "📝 Pending Leave Requests\n"
            response += "━━━━━━━━━━━━━━━━━━\n\n"

            for leave in leaves:
                response += (
                    f"🆔 ID: {leave['id']}\n"
                    f"👤 Employee: {leave['employee_id']}\n"
                    f"📅 {leave['start_date']} → {leave['end_date']}\n"
                    f"📝 {leave['reason']}\n\n"
                )

            return response

        # -------------------------
        # Approve
        # -------------------------
        if "approve" in text:

            match = re.search(r"\d+", text)

            if not match:
                return "❌ Example: Approve 3"

            leave_id = int(match.group())

            approve_leave(leave_id)

            return (
                f"✅ Leave #{leave_id} has been approved."
            )

        # -------------------------
        # Reject
        # -------------------------
        if "reject" in text:

            match = re.search(r"\d+", text)

            if not match:
                return "❌ Example: Reject 3"

            leave_id = int(match.group())

            reject_leave(leave_id)

            return (
                f"❌ Leave #{leave_id} has been rejected."
            )

        return "🤖 I couldn't understand your HR request."


hr_leave_skill = HRLeaveSkill()