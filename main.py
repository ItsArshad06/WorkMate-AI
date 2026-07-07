import os

from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler

from app.database.db import initialize_database
from app.handlers.start import start
from app.handlers.help import help_command

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")


def main():
    initialize_database()

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    print("🤖 WorkMate AI is online...")

    app.run_polling()


if __name__ == "__main__":
    main()