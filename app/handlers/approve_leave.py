from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

from app.database.leave import update_leave_status, leave_exists


async def approve_leave(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if len(context.args) != 1:
        await update.message.reply_text(
            "Usage: /approve <Leave ID>"
        )
        return


    leave_id = context.args[0]


    if not leave_exists(leave_id):
        await update.message.reply_text(
            "❌ Leave request not found."
        )
        return


    update_leave_status(
        leave_id,
        "Approved"
    )


    await update.message.reply_text(
        f"✅ Leave request {leave_id} has been approved."
    )



approve_leave_handler = CommandHandler(
    "approve",
    approve_leave
)