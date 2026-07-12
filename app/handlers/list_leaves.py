from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

from app.database.leave import get_all_leaves
from app.utils.auth import is_hr


async def list_leaves(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text(
            "Usage: /listleaves <Your Employee ID>"
        )
        return

    employee_id = context.args[0]

    if not is_hr(employee_id):
        await update.message.reply_text(
            "❌ You are not authorized to use this command."
        )
        return

    leaves = get_all_leaves()

    if not leaves:
        await update.message.reply_text("📂 No leave requests found.")
        return

    message = "📋 Leave Requests\n\n"

    for leave in leaves:
        message += (
            f"🆔 ID: {leave[0]}\n"
            f"👤 Employee: {leave[1]}\n"
            f"📅 From: {leave[2]}\n"
            f"📅 To: {leave[3]}\n"
            f"📝 Reason: {leave[4]}\n"
            f"📌 Status: {leave[5]}\n\n"
        )

    await update.message.reply_text(message)


list_leaves_handler = CommandHandler(
    "listleaves",
    list_leaves,
)