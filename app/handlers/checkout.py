from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

from app.database.employee import employee_exists
from app.database.attendance import check_out


async def checkout(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if len(context.args) != 1:
        await update.message.reply_text(
            "Usage: /checkout <Employee ID>"
        )
        return


    employee_id = context.args[0].upper()


    if not employee_exists(employee_id):
        await update.message.reply_text(
            "❌ Employee not found."
        )
        return


    result = check_out(employee_id)


    if result == "SUCCESS":

        await update.message.reply_text(
            f"✅ Check-out successful for {employee_id}."
        )


    elif result == "NOT_CHECKED_IN":

        await update.message.reply_text(
            "⚠️ You haven't checked in today."
        )


    elif result == "ALREADY_CHECKED_OUT":

        await update.message.reply_text(
            "⚠️ You have already checked out today."
        )


    else:

        await update.message.reply_text(
            "❌ Something went wrong."
        )



checkout_handler = CommandHandler(
    "checkout",
    checkout
)