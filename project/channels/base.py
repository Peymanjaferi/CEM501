class Channel:
    def fetch_messages(self):
        raise NotImplementedError

    def send_message(self, recipient, text):
        raise NotImplementedError

    @property
    def channel_name(self):
        raise NotImplementedError
