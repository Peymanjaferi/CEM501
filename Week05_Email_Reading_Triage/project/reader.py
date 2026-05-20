import imaplib
import email
from email.header import decode_header
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

IMAP_SERVER = os.getenv("IMAP_SERVER")
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")

EMAIL_COUNT = 20


def clean_text(text):
    """Remove HTML tags from email body."""
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()


def categorize_email(subject, body):
    """Assign category based on keywords."""
    content = f"{subject} {body}".lower()

    urgent_keywords = ["urgent", "asap", "immediately", "delay"]
    action_keywords = ["review", "approve", "response required", "action"]
    archive_keywords = ["newsletter", "promotion", "sale"]

    if any(word in content for word in urgent_keywords):
        return "URGENT"
    elif any(word in content for word in action_keywords):
        return "ACTION"
    elif any(word in content for word in archive_keywords):
        return "ARCHIVE"
    else:
        return "FYI"


def fetch_emails():
    mail = None

    try:
        # Connect to IMAP server
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)

        # Login
        mail.login(EMAIL_USER, EMAIL_PASS)

        # Select inbox
        mail.select("inbox")

        # Search emails
        status, messages = mail.search(None, "ALL")

        email_ids = messages[0].split()
        recent_emails = email_ids[-EMAIL_COUNT:]

        results = []

        for email_id in reversed(recent_emails):
            status, msg_data = mail.fetch(email_id, "(RFC822)")

            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])

                    # Decode subject
                    subject, encoding = decode_header(msg["Subject"])[0]

                    if isinstance(subject, bytes):
                        subject = subject.decode(
                            encoding if encoding else "utf-8"
                        )

                    sender = msg.get("From")
                    date = msg.get("Date")

                    body = ""

                    if msg.is_multipart():
                        for part in msg.walk():
                            content_type = part.get_content_type()

                            if content_type == "text/plain":
                                try:
                                    body = part.get_payload(decode=True).decode()
                                except:
                                    pass

                            elif content_type == "text/html":
                                try:
                                    html = part.get_payload(decode=True).decode()
                                    body = clean_text(html)
                                except:
                                    pass
                    else:
                        body = msg.get_payload(decode=True).decode()

                    preview = body[:200].replace("\n", " ")

                    category = categorize_email(subject, preview)

                    results.append({
                        "category": category,
                        "sender": sender,
                        "subject": subject,
                        "date": date,
                        "preview": preview
                    })

        # Sort emails by priority
        priority_order = {
            "URGENT": 0,
            "ACTION": 1,
            "FYI": 2,
            "ARCHIVE": 3
        }

        results.sort(key=lambda x: priority_order[x["category"]])

        # Print summary
        for email_item in results:
            print("=" * 60)
            print(f"Category: {email_item['category']}")
            print(f"From: {email_item['sender']}")
            print(f"Subject: {email_item['subject']}")
            print(f"Date: {email_item['date']}")
            print(f"Preview: {email_item['preview']}")
            print("=" * 60)

    finally:
        # Close connection
        if mail:
            mail.logout()


if __name__ == "__main__":
    fetch_emails()
