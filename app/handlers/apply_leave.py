from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

from app.database.leave import create_leave
from app.database.session import get_session


async def apply_leave(update: Update, context: ContextTypes.DEFAULT_TYPE):

    telegram_user_id = update.effective_user.id

    session = get_session(telegram_user_id)

    if session is None:
        await update.message.reply_text(
            "❌ Please login first using /login"
        )
        return


    if len(context.args) < 3:
        await update.message.reply_text(
            "Usage:\n"
            "/applyleave <start_date> <end_date> <reason>\n\n"
            "Example:\n"
            "/applyleave 2026-07-21 2026-07-22 Fever"
        )
        return


    employee_id = session["employee_id"]

    start_date = context.args[0]

    end_date = context.args[1]

    reason = " ".join(context.args[2:])


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
    apply_leave
)