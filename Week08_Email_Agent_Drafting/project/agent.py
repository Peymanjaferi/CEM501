import argparse
from datetime import datetime

# Sample emails (used if reader.py is unavailable)
sample_emails = [
    {
        "sender": "architect@project.com",
        "subject": "RFI-047 Response",
        "body": "The revised rebar spacing has been approved.",
        "triage_category": "ACTION"
    },
    {
        "sender": "owner@university.edu",
        "subject": "Urgent Schedule Update",
        "body": "Please provide a recovery schedule by tomorrow.",
        "triage_category": "URGENT"
    },
    {
        "sender": "newsletter@construction.com",
        "subject": "Industry Newsletter",
        "body": "Latest construction industry news.",
        "triage_category": "FYI"
    }
]

KNOWN_CONTACTS = [
    "architect@project.com",
    "owner@university.edu"
]


def fetch_emails():
    """Returns sample emails."""
    return sample_emails


def generate_draft(email):
    """Creates a simple reply draft."""
    return f"""
Dear Sender,

Thank you for your email regarding "{email['subject']}".

We have reviewed your message and will take the necessary action.

Best Regards,
Project Manager
"""


def validate_email(recipient, subject, body):
    """Basic guardrails."""

    if recipient not in KNOWN_CONTACTS:
        print("WARNING: Unknown recipient.")

    if subject.strip() == "":
        print("WARNING: Empty subject.")

    if "[TODO]" in body or "[INSERT]" in body:
        print("WARNING: Placeholder text detected.")


def log_email(recipient, subject):
    """Logs sent emails."""

    with open("sent_log.txt", "a") as f:
        f.write(
            f"{datetime.now()} | {recipient} | {subject}\n"
        )


def send_email(recipient, subject, body, dry_run=False):
    """Human approval before sending."""

    print("\n" + "=" * 50)
    print("TO:", recipient)
    print("SUBJECT:", subject)
    print("BODY:")
    print(body)
    print("=" * 50)

    validate_email(recipient, subject, body)

    if dry_run:
        print("DRY RUN: Email not sent.\n")
        return

    choice = input(
        "Send email? (y = send, n = skip, e = edit): "
    )

    if choice.lower() == "y":
        print("Email sent successfully.")
        log_email(recipient, subject)

    elif choice.lower() == "e":
        print("Edit in your editor and rerun.")

    else:
        print("Skipped.")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show drafts without sending"
    )

    args = parser.parse_args()

    emails = fetch_emails()

    print("\n=== EMAIL AGENT V1 ===\n")

    for email in emails:

        category = email["triage_category"]

        print(
            f"[{category}] {email['subject']} "
            f"from {email['sender']}"
        )

        if category in ["URGENT", "ACTION"]:

            draft = generate_draft(email)

            send_email(
                recipient=email["sender"],
                subject="RE: " + email["subject"],
                body=draft,
                dry_run=args.dry_run
            )


if __name__ == "__main__":
    main()
