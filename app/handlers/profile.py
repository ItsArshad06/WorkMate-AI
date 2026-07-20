from telegram import Update
from telegram.ext import (
    ContextTypes,
    CommandHandler,
)

from app.database.session import get_session


async def profile(update: Update, context: ContextTypes.DEFAULT_TYPE):

    telegram_user_id = update.effective_user.id

    session = get_session(telegram_user_id)

    if session is None:
        await update.message.reply_text(
            "❌ You are not logged in.\n\nUse /login first."
        )
        return

    await update.message.reply_text(
        f"👤 Employee Profile\n\n"
        f"Name: {session['employee_name']}\n"
        f"Employee ID: {session['employee_id']}\n"
        f"Department: {session['department']}\n"
        f"Role: {session['role']}"
    )


profile_handler = CommandHandler(
    "myprofile",
    profile
)