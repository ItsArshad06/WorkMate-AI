from telegram import Update
from telegram.ext import (
    ContextTypes,
    ConversationHandler,
    CommandHandler,
    MessageHandler,
    filters,
)

from app.database.employee import get_employee

EMPLOYEE_ID = 0


async def profile(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🆔 Enter your Employee ID:")
    return EMPLOYEE_ID


async def show_profile(update: Update, context: ContextTypes.DEFAULT_TYPE):
    employee_id = update.message.text

    employee = get_employee(employee_id)

    if employee:
        await update.message.reply_text(
            f"👤 Employee Profile\n\n"
            f"Name: {employee[0]}\n"
            f"Employee ID: {employee[1]}\n"
            f"Department: {employee[2]}\n"
            f"Phone: {employee[3]}"
        )
    else:
        await update.message.reply_text("❌ Employee not found.")

    return ConversationHandler.END


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Cancelled.")
    return ConversationHandler.END


profile_handler = ConversationHandler(
    entry_points=[CommandHandler("myprofile", profile)],
    states={
        EMPLOYEE_ID: [
            MessageHandler(filters.TEXT & ~filters.COMMAND, show_profile)
        ]
    },
    fallbacks=[CommandHandler("cancel", cancel)],
)