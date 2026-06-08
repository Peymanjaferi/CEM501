from abc import ABC, abstractmethod

class Channel(ABC):

    @abstractmethod
    def fetch_messages(self):
        pass

    @abstractmethod
    def send_message(self, recipient, text):
        pass

    @property
    @abstractmethod
    def channel_name(self):
        pass
