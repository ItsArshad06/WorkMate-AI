from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

from app.database.attendance import get_today_attendance
from app.utils.auth import is_hr


async def attendance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) != 1:
        await update.message.reply_text(
            "Usage: /attendance <Your Employee ID>"
        )
        return

    employee_id = context.args[0].upper()

    if not is_hr(employee_id):
        await update.message.reply_text(
            "❌ You are not authorized to view attendance."
        )
        return

    records = get_today_attendance()

    if not records:
        await update.message.reply_text(
            "📂 No attendance records found for today."
        )
        return

    message = "📅 Today's Attendance\n\n"

    for i, record in enumerate(records, start=1):
        checkout = record["check_out"] if record["check_out"] else "Not Checked Out"

        message += (
            f"{i}. Employee ID: {record['employee_id']}\n"
            f"   Check In : {record['check_in']}\n"
            f"   Check Out: {checkout}\n\n"
        )

    await update.message.reply_text(message)


attendance_handler = CommandHandler(
    "attendance",
    attendance,
)