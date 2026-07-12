from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

from app.ai.brain import brain


async def ai_chat(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.effective_user.id

    if context.args:
        message = " ".join(context.args)
    else:
        await update.message.reply_text(
            "💬 Talk to me.\nExample:\n/chat I need leave tomorrow"
        )
        return

    reply = brain.process(user_id, message)

    await update.message.reply_text(reply)


ai_chat_handler = CommandHandler(
    "chat",
    ai_chat,
)