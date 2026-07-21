from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

from app.database.employee import get_employee
from app.database.password import get_password_hash
from app.database.session import save_session
from app.security.security import verify_password


async def login(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if len(context.args) != 2:
        await update.message.reply_text(
            "Usage:\n/login <Employee ID> <Password>\n\n"
            "Example:\n/login EMP-101 Welcome123"
        )
        return

    employee_id = context.args[0].upper()
    password = context.args[1]

    employee = get_employee(employee_id)

    if employee is None:
        await update.message.reply_text(
            "❌ Employee not found."
        )
        return

    password_hash = get_password_hash(employee_id)

    if password_hash is None:
        await update.message.reply_text(
            "❌ Password has not been set for this employee."
        )
        return

    if not verify_password(password, password_hash):
        await update.message.reply_text(
            "❌ Invalid password."
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