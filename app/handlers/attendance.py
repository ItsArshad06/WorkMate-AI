from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

from app.database.session import get_session
from app.database.attendance import (
    check_in,
    check_out,
    get_today_attendance
)


async def checkin(update: Update, context: ContextTypes.DEFAULT_TYPE):

    telegram_user_id = update.effective_user.id

    session = get_session(telegram_user_id)

    if session is None:
        await update.message.reply_text(
            "❌ Please login first using /login"
        )
        return

    result = check_in(session["employee_id"])

    if result == "SUCCESS":
        await update.message.reply_text(
            "✅ Check-in successful"
        )

    elif result == "ALREADY_CHECKED_IN":
        await update.message.reply_text(
            "⚠️ You already checked in today."
        )


async def checkout(update: Update, context: ContextTypes.DEFAULT_TYPE):

    telegram_user_id = update.effective_user.id

    session = get_session(telegram_user_id)

    if session is None:
        await update.message.reply_text(
            "❌ Please login first using /login"
        )
        return

    result = check_out(session["employee_id"])

    if result == "SUCCESS":
        await update.message.reply_text(
            "✅ Check-out successful"
        )

    elif result == "NOT_CHECKED_IN":
        await update.message.reply_text(
            "⚠️ You haven't checked in today."
        )

    elif result == "ALREADY_CHECKED_OUT":
        await update.message.reply_text(
            "⚠️ You already checked out."
        )


async def attendance(update: Update, context: ContextTypes.DEFAULT_TYPE):

    records = get_today_attendance()

    if not records:
        await update.message.reply_text(
            "📂 No attendance records found today."
        )
        return


    message = "📅 Today's Attendance\n\n"


    for record in records:

        message += (
            f"👤 Employee: {record['employee_id']}\n"
            f"🟢 Check In: {record['check_in']}\n"
            f"🔴 Check Out: {record['check_out'] or 'Not checked out'}\n\n"
        )


    await update.message.reply_text(message)



attendance_handler = [
    CommandHandler("checkin", checkin),
    CommandHandler("checkout", checkout),
    CommandHandler("attendance", attendance),
]