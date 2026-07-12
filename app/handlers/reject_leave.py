from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

from app.database.leave import update_leave_status
from app.utils.auth import is_hr


async def reject_leave(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) != 2:
        await update.message.reply_text(
            "Usage: /rejectleave <Your Employee ID> <Leave ID>"
        )
        return

    employee_id = context.args[0]
    leave_id = context.args[1]

    if not is_hr(employee_id):
        await update.message.reply_text(
            "❌ You are not authorized to reject leaves."
        )
        return

    update_leave_status(leave_id, "Rejected")

    await update.message.reply_text(
        f"❌ Leave request {leave_id} has been rejected."
    )


reject_leave_handler = CommandHandler(
    "rejectleave",
    reject_leave,
)