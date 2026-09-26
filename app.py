import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Logging setup
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Bot token from Environment Variable
BOT_TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! آپ کا 24/7 بوٹ کام کر رہا ہے۔")

if __name__ == '__main__':
    if not BOT_TOKEN:
        print("Error: BOT_TOKEN Environment Variable is missing!")
    else:
        app = ApplicationBuilder().token(BOT_TOKEN).build()
        app.add_handler(CommandHandler("start", start))
        print("Bot is running...")
        app.run_polling()
