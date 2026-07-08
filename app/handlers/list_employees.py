from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

from app.database.employee import get_all_employees


async def list_employees(update: Update, context: ContextTypes.DEFAULT_TYPE):
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
    list_employees
)