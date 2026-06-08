class Channel:
    """Base class — every communication channel must implement these methods."""

    def fetch_messages(self) -> list[dict]:
        """Pull new incoming messages from this channel."""
        raise NotImplementedError

    def send_message(self, recipient: str, text: str) -> bool:
        """Send a message through this channel. Returns True if successful."""
        raise NotImplementedError

    @property
    def channel_name(self) -> str:
        """Human-readable name of this channel (e.g., 'email', 'telegram')."""
        raise NotImplementedError
