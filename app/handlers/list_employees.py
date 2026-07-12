from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

from app.database.employee import get_all_employees
from app.utils.auth import is_hr


async def list_employees(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text(
            "Usage: /listemployees <Your Employee ID>"
        )
        return

    employee_id = context.args[0]

    if not is_hr(employee_id):
        await update.message.reply_text(
            "❌ You are not authorized to use this command."
        )
        return

    employees = get_all_employees()

    if not employees:
        await update.message.reply_text("📂 No employees found.")
        return

    message = "👥 Employee List\n\n"

    for i, employee in enumerate(employees, start=1):
        message += (
            f"{i}. {employee[0]}\n"
            f"   ID: {employee[1]}\n"
            f"   Department: {employee[2]}\n\n"
        )

    await update.message.reply_text(message)


list_employees_handler = CommandHandler(
    "listemployees",
    list_employees,
)