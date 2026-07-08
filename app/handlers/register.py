from telegram import Update
from telegram.ext import (
    ContextTypes,
    ConversationHandler,
    CommandHandler,
    MessageHandler,
    filters,
)

from app.database.employee import save_employee, employee_exists

NAME, EMPLOYEE_ID, DEPARTMENT, PHONE = range(4)


async def register(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👤 Enter your full name:")
    return NAME


async def get_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["full_name"] = update.message.text.strip()
    await update.message.reply_text("🆔 Enter your Employee ID:")
    return EMPLOYEE_ID


async def get_employee_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    employee_id = update.message.text.strip().upper()

    if employee_exists(employee_id):
        await update.message.reply_text(
            "❌ Employee ID already exists.\nPlease enter a different Employee ID:"
        )
        return EMPLOYEE_ID

    context.user_data["employee_id"] = employee_id
    await update.message.reply_text("🏢 Enter your Department:")
    return DEPARTMENT


async def get_department(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["department"] = update.message.text.strip()
    await update.message.reply_text("📱 Enter your Phone Number:")
    return PHONE


async def get_phone(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["phone"] = update.message.text.strip()

    save_employee(
        context.user_data["full_name"],
        context.user_data["employee_id"],
        context.user_data["department"],
        context.user_data["phone"],
    )

    await update.message.reply_text(
        "✅ Registration completed successfully!"
    )

    return ConversationHandler.END


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("❌ Registration cancelled.")
    return ConversationHandler.END


register_handler = ConversationHandler(
    entry_points=[CommandHandler("register", register)],
    states={
        NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_name)],
        EMPLOYEE_ID: [
            MessageHandler(filters.TEXT & ~filters.COMMAND, get_employee_id)
        ],
        DEPARTMENT: [
            MessageHandler(filters.TEXT & ~filters.COMMAND, get_department)
        ],
        PHONE: [
            MessageHandler(filters.TEXT & ~filters.COMMAND, get_phone)
        ],
    },
    fallbacks=[CommandHandler("cancel", cancel)],
)