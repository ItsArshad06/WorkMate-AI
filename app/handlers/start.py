from telegram import Update
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "👋 Hello!\n\n"
        "Welcome to WorkMate AI.\n\n"
        "I can help you with HR tasks.\n\n"
        "Just tell me what you need:\n\n"
        "• I need leave\n"
        "• Show my profile\n"
        "• Check attendance\n"
        "• Help"
    )