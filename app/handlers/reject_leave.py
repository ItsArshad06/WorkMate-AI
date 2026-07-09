from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

from app.database.leave import update_leave_status


async def reject_leave(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) != 1:
        await update.message.reply_text(
            "Usage: /rejectleave <Leave ID>"
        )
        return

    leave_id = context.args[0]

    update_leave_status(leave_id, "Rejected")

    await update.message.reply_text(
        f"❌ Leave request {leave_id} has been rejected."
    )


reject_leave_handler = CommandHandler(
    "rejectleave",
    reject_leave,
)