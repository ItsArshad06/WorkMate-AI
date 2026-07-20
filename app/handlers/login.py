from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

from app.database.employee import get_employee
from app.database.session import save_session


async def login(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if len(context.args) != 1:
        await update.message.reply_text(
            "Usage:\n/login <Employee ID>\n\nExample:\n/login EMP-101"
        )
        return


    employee_id = context.args[0].upper()


    employee = get_employee(employee_id)


    if employee is None:
        await update.message.reply_text(
            "❌ Employee not found."
        )
        return


    telegram_user_id = update.effective_user.id


    save_session(
        telegram_user_id,
        employee["employee_id"],
        employee["role"],
        employee["full_name"],
        employee["department"]
    )


    await update.message.reply_text(
        f"✅ Login successful!\n\n"
        f"Welcome {employee['full_name']} 👋\n"
        f"Department: {employee['department']}"
    )


login_handler = CommandHandler(
    "login",
    login
)