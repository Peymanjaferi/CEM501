# This code works with 1 channel or 10 channels — no changes needed
active_channels = [EmailChannel(), TelegramChannel()]

for channel in active_channels:
    new_messages = channel.fetch_messages()
    for msg in new_messages:
        category = classifier.classify(msg["text"])
        draft = drafter.draft(msg["text"], category)
        channel.send_message(msg["sender"], draft)
        print(f"[{channel.channel_name}] Replied to {msg['sender']}: {category}")
