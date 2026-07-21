from telegram import Update
from telegram.ext import ContextTypes, MessageHandler, filters

from app.database.session import get_session
from app.services.ai_service import ask_ai


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not update.message:
        return

    telegram_user_id = update.effective_user.id

    session = get_session(telegram_user_id)

    if session is None:
        await update.message.reply_text(
            "👋 Please login first using:\n\n/login <Employee ID>"
        )
        return

    message = update.message.text.strip()

    reply = ask_ai(
        session["employee_id"],
        message
    )

    await update.message.reply_text(reply)


message_handler = MessageHandler(
    filters.TEXT & ~filters.COMMAND,
    handle_message,
)