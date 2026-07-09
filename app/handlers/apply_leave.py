from telegram import Update
from telegram.ext import (
    ContextTypes,
    ConversationHandler,
    CommandHandler,
    MessageHandler,
    filters,
)

from app.database.leave import create_leave

EMPLOYEE_ID, START_DATE, END_DATE, REASON = range(4)


async def apply_leave(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🆔 Enter your Employee ID:")
    return EMPLOYEE_ID


async def get_employee_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["employee_id"] = update.message.text.strip().upper()

    await update.message.reply_text("📅 Enter Start Date (DD/MM/YYYY):")
    return START_DATE


async def get_start_date(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["start_date"] = update.message.text.strip()

    await update.message.reply_text("📅 Enter End Date (DD/MM/YYYY):")
    return END_DATE


async def get_end_date(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["end_date"] = update.message.text.strip()

    await update.message.reply_text("📝 Enter Leave Reason:")
    return REASON


async def get_reason(update: Update, context: ContextTypes.DEFAULT_TYPE):
    create_leave(
        context.user_data["employee_id"],
        context.user_data["start_date"],
        context.user_data["end_date"],
        update.message.text.strip(),
    )

    await update.message.reply_text("✅ Leave request submitted successfully!")

    return ConversationHandler.END


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("❌ Leave request cancelled.")
    return ConversationHandler.END


apply_leave_handler = ConversationHandler(
    entry_points=[CommandHandler("applyleave", apply_leave)],
    states={
        EMPLOYEE_ID: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_employee_id)],
        START_DATE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_start_date)],
        END_DATE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_end_date)],
        REASON: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_reason)],
    },
    fallbacks=[CommandHandler("cancel", cancel)],
)