import os

from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler

from app.database.db import initialize_database


# Basic commands
from app.handlers.start import start
from app.handlers.help import help_command


# Authentication
from app.handlers.login import login_handler


# Employee features
from app.handlers.profile import profile_handler
from app.handlers.mydashboard import mydashboard_handler
from app.handlers.list_employees import list_employees_handler


# Leave features
from app.handlers.apply_leave import apply_leave_handler
from app.handlers.list_leaves import list_leaves_handler
from app.handlers.approve_leave import approve_leave_handler
from app.handlers.reject_leave import reject_leave_handler


# Attendance
from app.handlers.attendance import attendance_handler


# Dashboard
from app.handlers.dashboard import dashboard_handler


# AI chat
from app.handlers.message_handler import message_handler


load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")


def main():

    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN not found!")

    initialize_database()

    app = Application.builder().token(BOT_TOKEN).build()

    # =====================
    # Basic Commands
    # =====================

    app.add_handler(
        CommandHandler("start", start)
    )

    app.add_handler(
        CommandHandler("help", help_command)
    )

    # =====================
    # Authentication
    # =====================

    app.add_handler(login_handler)

    # =====================
    # Employee Features
    # =====================

    app.add_handler(profile_handler)
    app.add_handler(mydashboard_handler)
    app.add_handler(list_employees_handler)

    # =====================
    # Leave Management
    # =====================

    app.add_handler(apply_leave_handler)
    app.add_handler(list_leaves_handler)
    app.add_handler(approve_leave_handler)
    app.add_handler(reject_leave_handler)

    # =====================
    # Attendance
    # =====================

    for handler in attendance_handler:
        app.add_handler(handler)

    # =====================
    # Dashboard
    # =====================

    app.add_handler(dashboard_handler)

    # =====================
    # AI Assistant
    # Keep this LAST
    # =====================

    app.add_handler(message_handler)

    print("🤖 WorkMate AI Telegram Bot is running...")

    app.run_polling()


if __name__ == "__main__":
    main()