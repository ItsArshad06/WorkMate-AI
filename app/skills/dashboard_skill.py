from app.ai.session import session
from app.utils.auth import is_hr

from app.database.employee import get_employee_count
from app.database.leave import (
    get_pending_leave_count,
    get_approved_leave_count,
    get_rejected_leave_count,
)
from app.database.attendance import get_today_attendance


class DashboardSkill:

    def execute(self, user_id, message):

        employee_id = session.employee_id(user_id)

        if employee_id is None:
            return (
                "🔐 Please login first.\n"
                "Enter your Employee ID."
            )

        if not is_hr(employee_id):
            return "❌ You are not authorized to view the HR dashboard."

        total_employees = get_employee_count()
        pending = get_pending_leave_count()
        approved = get_approved_leave_count()
        rejected = get_rejected_leave_count()
        attendance = len(get_today_attendance())

        return (
            "🤖 WorkMate AI Dashboard\n"
            "━━━━━━━━━━━━━━━━━━\n\n"
            f"👥 Total Employees : {total_employees}\n"
            f"📅 Today's Attendance : {attendance}\n"
            f"📝 Pending Leaves : {pending}\n"
            f"✅ Approved Leaves : {approved}\n"
            f"❌ Rejected Leaves : {rejected}\n\n"
            "━━━━━━━━━━━━━━━━━━\n"
            "⚡ HR System Status: Online"
        )


dashboard_skill = DashboardSkill()