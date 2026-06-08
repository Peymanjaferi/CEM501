import os
from dotenv import load_dotenv
from telegram import Bot

from channels.base import Channel

load_dotenv()

class TelegramChannel(Channel):

    @property
    def channel_name(self):
        return "telegram"

    def fetch_messages(self):
        return []

    def send_message(self, chat_id, text):
        try:
            bot = Bot(token=os.getenv("TELEGRAM_BOT_TOKEN"))
            bot.send_message(chat_id=chat_id, text=text)
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
