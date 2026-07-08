import os

from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler

from app.database.db import initialize_database
from app.handlers.start import start
from app.handlers.help import help_command
from app.handlers.register import register_handler
from app.handlers.profile import profile_handler

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")


def main():
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN not found!")

    initialize_database()

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(register_handler)
    app.add_handler(profile_handler)

    print("🤖 WorkMate AI is online...")

    app.run_polling()


if __name__ == "__main__":
    main()