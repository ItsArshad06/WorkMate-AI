from telegram import Update
from telegram.ext import ContextTypes


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 WorkMate AI\n\n"
        "Available Commands:\n\n"
        "/start - Start the bot\n"
        "/help - Show this menu\n"
        "/register - Register as an employee (Coming Soon)\n\n"
        "Version: 0.1.0"
    )