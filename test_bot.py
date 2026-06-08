import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    filters,
    ContextTypes
)

load_dotenv()

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"You said: {update.message.text}"
    )

app = (
    ApplicationBuilder()
    .token(os.getenv("TELEGRAM_BOT_TOKEN"))
    .build()
)

app.add_handler(
    MessageHandler(filters.TEXT, echo)
)

print("Bot running...")
app.run_polling()
