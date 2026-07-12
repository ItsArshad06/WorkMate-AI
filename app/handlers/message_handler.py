from telegram import Update
from telegram.ext import ContextTypes, MessageHandler, filters

from app.ai.brain import brain


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not update.message or not update.message.text:
        return

    user_id = update.effective_user.id
    message = update.message.text.strip()

    reply = brain.process(user_id, message)

    await update.message.reply_text(reply)


message_handler = MessageHandler(
    filters.TEXT & ~filters.COMMAND,
    handle_message,
)