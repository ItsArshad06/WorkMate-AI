from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

from app.database.session import get_session
from app.database.employee import get_employee
from app.database.leave import get_employee_leave_summary
from app.database.attendance import get_employee_attendance


async def mydashboard(update: Update, context: ContextTypes.DEFAULT_TYPE):

    telegram_user_id = update.effective_user.id

    session = get_session(telegram_user_id)

    if session is None:
        await update.message.reply_text(
            "❌ Please login first using /login"
        )
        return

    employee = get_employee(session["employee_id"])

    if employee is None:
        await update.message.reply_text(
            "❌ Employee not found."
        )
        return

    leave_summary = get_employee_leave_summary(
        session["employee_id"]
    )

    attendance = get_employee_attendance(
        session["employee_id"]
    )

    status = "❌ No Attendance"
    check_in = "-"
    check_out = "-"

    if attendance:

        latest = attendance[0]

        status = "✅ Present"
        check_in = latest["check_in"] or "-"
        check_out = latest["check_out"] or "Not checked out"

    message = (
        "👤 Employee Dashboard\n\n"
        f"Name: {employee['full_name']}\n"
        f"Employee ID: {employee['employee_id']}\n"
        f"Department: {employee['department']}\n\n"
        f"📅 Attendance\n"
        f"Status: {status}\n"
        f"Check In: {check_in}\n"
        f"Check Out: {check_out}\n\n"
        f"📝 Leave Summary\n"
        f"Pending : {leave_summary['Pending']}\n"
        f"Approved: {leave_summary['Approved']}\n"
        f"Rejected: {leave_summary['Rejected']}"
    )

    await update.message.reply_text(message)


mydashboard_handler = CommandHandler(
    "mydashboard",
    mydashboard,
)