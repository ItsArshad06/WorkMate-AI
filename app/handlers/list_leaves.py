from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

from app.database.leave import get_all_leaves
from app.utils.auth import is_hr


async def list_leaves(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not context.args:
        await update.message.reply_text(
            "Usage: /leaves <Your Employee ID>"
        )
        return


    employee_id = context.args[0].upper()


    if not is_hr(employee_id):
        await update.message.reply_text(
            "❌ You are not authorized to use this command."
        )
        return


    leaves = get_all_leaves()


    if not leaves:
        await update.message.reply_text(
            "📂 No leave requests found."
        )
        return


    message = "📋 Leave Requests\n\n"


    for leave in leaves:

        message += (
            f"🆔 ID: {leave['id']}\n"
            f"👤 Employee: {leave['employee_id']}\n"
            f"📅 From: {leave['start_date']}\n"
            f"📅 To: {leave['end_date']}\n"
            f"📝 Reason: {leave['reason']}\n"
            f"📌 Status: {leave['status']}\n\n"
        )


    await update.message.reply_text(message)



list_leaves_handler = CommandHandler(
    "leaves",
    list_leaves
)