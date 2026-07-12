from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

from app.database.leave import create_leave


async def apply_leave(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 4:
        await update.message.reply_text(
            "Usage: /applyleave <Employee ID> <Start Date> <End Date> <Reason>"
        )
        return

    employee_id = context.args[0]
    start_date = context.args[1]
    end_date = context.args[2]
    reason = " ".join(context.args[3:])

    create_leave(
        employee_id,
        start_date,
        end_date,
        reason
    )

    await update.message.reply_text(
        "✅ Leave request submitted successfully."
    )


apply_leave_handler = CommandHandler(
    "applyleave",
    apply_leave,
)