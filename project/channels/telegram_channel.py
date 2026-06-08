class EmailChannel(Channel):
    channel_name = "email"

    def fetch_messages(self):
        # Uses IMAP to connect to inbox and pull new emails
        ...

    def send_message(self, recipient, text):
        # Uses SMTP to send an email
        ...


class TelegramChannel(Channel):
    channel_name = "telegram"

    def fetch_messages(self):
        # Uses Telegram Bot API to get new messages
        ...

    def send_message(self, recipient, text):
        # Uses Telegram Bot API to send a reply
        ...
