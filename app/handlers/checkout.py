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

    success = check_out(employee_id)

    if success:
        await update.message.reply_text(
            f"✅ Check-out successful for {employee_id}."
        )
    else:
        await update.message.reply_text(
            "⚠️ You haven't checked in today or have already checked out."
        )


checkout_handler = CommandHandler(
    "checkout",
    checkout,
)