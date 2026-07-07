import os

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Hello Arshu!\nWelcome to WorkMate AI!"
    )


def main():
    if TOKEN is None:
        raise RuntimeError("BOT_TOKEN not loaded!")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Bot started...")

    app.run_polling()


if __name__ == "__main__":
    main()