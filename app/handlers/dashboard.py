from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

from app.utils.auth import is_hr
from app.database.employee import get_employee_count
from app.database.leave import (
    get_pending_leave_count,
    get_approved_leave_count,
    get_rejected_leave_count,
)


async def dashboard(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if len(context.args) != 1:
        await update.message.reply_text(
            "Usage: /dashboard <HR Employee ID>"
        )
        return

    employee_id = context.args[0].upper()

    if not is_hr(employee_id):
        await update.message.reply_text(
            "❌ You are not authorized to view the dashboard."
        )
        return

    total_employees = get_employee_count()
    pending = get_pending_leave_count()
    approved = get_approved_leave_count()
    rejected = get_rejected_leave_count()

    message = (
        "🤖 WorkMate AI Dashboard\n"
        "━━━━━━━━━━━━━━━━━━\n\n"
        f"👥 Total Employees : {total_employees}\n"
        f"📝 Pending Leaves : {pending}\n"
        f"✅ Approved Leaves : {approved}\n"
        f"❌ Rejected Leaves : {rejected}\n\n"
        "━━━━━━━━━━━━━━━━━━\n"
        "⚡ HR System Status: Online"
    )

    await update.message.reply_text(message)


dashboard_handler = CommandHandler(
    "dashboard",
    dashboard,
)