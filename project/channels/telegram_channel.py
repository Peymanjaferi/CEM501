import os
from dotenv import load_dotenv

load_dotenv()

class TelegramChannel:
    """
    Telegram communication channel.
    """

    channel_name = "telegram"

    def __init__(self):
        self.token = os.getenv("TELEGRAM_BOT_TOKEN")

        if not self.token:
            raise ValueError(
                "TELEGRAM_BOT_TOKEN not found in .env"
            )

    def fetch_messages(self):
        """
        Placeholder for fetching messages.
        """
        return []

    def send_message(self, recipient, text):
        """
        Send a Telegram message.
        """
        print(f"Sending Telegram message to {recipient}")
        return True
