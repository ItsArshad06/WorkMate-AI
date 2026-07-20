from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

from app.database.employee import employee_exists
from app.database.attendance import check_in


async def checkin(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if len(context.args) != 1:
        await update.message.reply_text(
            "Usage: /checkin <Employee ID>"
        )
        return


    employee_id = context.args[0].upper()


    if not employee_exists(employee_id):
        await update.message.reply_text(
            "❌ Employee not found."
        )
        return


    result = check_in(employee_id)


    if result == "SUCCESS":

        await update.message.reply_text(
            f"✅ Check-in successful for {employee_id}."
        )

    elif result == "ALREADY_CHECKED_IN":

        await update.message.reply_text(
            "⚠️ You have already checked in today."
        )

    else:

        await update.message.reply_text(
            "❌ Something went wrong."
        )



checkin_handler = CommandHandler(
    "checkin",
    checkin
)