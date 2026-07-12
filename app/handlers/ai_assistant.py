from telegram import Update
from telegram.ext import ContextTypes, MessageHandler, filters

from app.database.employee import employee_exists


async def ai_assistant(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        return

    text = update.message.text.strip().lower()

    # Ignore commands like /start, /help, etc.
    if text.startswith("/"):
        return

    # -------- Leave Intent --------
    if "leave" in text:
        await update.message.reply_text(
            "📝 It looks like you want to apply for leave.\n\n"
            "Use:\n"
            "/applyleave <Employee ID> <Start Date> <End Date> <Reason>"
        )
        return

    # -------- Profile Intent --------
    elif "profile" in text or "my profile" in text:
        await update.message.reply_text(
            "👤 To view your profile use:\n"
            "/myprofile"
        )
        return

    # -------- Dashboard Intent --------
    elif "dashboard" in text:
        await update.message.reply_text(
            "📊 HR Dashboard:\n"
            "Use /dashboard"
        )
        return

    # -------- Employee List --------
    elif "employee" in text or "employees" in text:
        await update.message.reply_text(
            "👥 To view employees use:\n"
            "/listemployees <HR Employee ID>"
        )
        return

    # -------- Attendance --------
    elif "attendance" in text:
        await update.message.reply_text(
            "🕒 Attendance module is available."
        )
        return

    # -------- Greetings --------
    elif text in ["hi", "hello", "hey", "assalamu alaikum", "assalamualaikum"]:
        await update.message.reply_text(
            "👋 Hello! I'm WorkMate AI.\n"
            "How can I help you today?"
        )
        return

    # -------- Unknown --------
    else:
        await update.message.reply_text(
            "🤖 I'm still learning.\n\n"
            "Try asking about:\n"
            "• Leave\n"
            "• Profile\n"
            "• Employees\n"
            "• Dashboard\n"
            "• Attendance"
        )


ai_assistant_handler = MessageHandler(
    filters.TEXT & ~filters.COMMAND,
    ai_assistant,
)