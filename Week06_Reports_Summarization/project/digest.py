from datetime import datetime


def summarize_email(body):
    """
    Simple one-line summary generator.
    """
    sentences = body.split(".")
    return sentences[0].strip() + "." if sentences else body[:100]


def group_by_category(emails):
    """
    Group emails by triage category.
    """
    grouped = {
        "URGENT": [],
        "ACTION": [],
        "FYI": [],
        "ARCHIVE": []
    }

    for email in emails:
        category = email.get("triage_category", "FYI")

        if category in grouped:
            grouped[category].append(email)

    return grouped


def print_digest(emails):
    """
    Print formatted morning digest.
    """

    grouped = group_by_category(emails)

    now = datetime.now().strftime("%B %d, %Y at %H:%M")

    print("=" * 50)
    print("=== PROJECT MORNING DIGEST ===")
    print(f"Generated: {now}")
    print(f"Covering: {len(emails)} emails")
    print("=" * 50)

    # URGENT
    print(f"\n--- URGENT ({len(grouped['URGENT'])}) ---")

    for i, email in enumerate(grouped["URGENT"], start=1):
        summary = summarize_email(email["body"])

        print(f"[{i}] From: {email['sender']}")
        print(f"    Subject: {email['subject']}")
        print(f"    Summary: {summary}")
        print()

    # ACTION
    print(f"\n--- ACTION ({len(grouped['ACTION'])}) ---")

    for i, email in enumerate(grouped["ACTION"], start=1):
        summary = summarize_email(email["body"])

        print(f"[{i}] From: {email['sender']}")
        print(f"    Subject: {email['subject']}")
        print(f"    Summary: {summary}")
        print()

    # FYI
    print(f"\n--- FYI ({len(grouped['FYI'])}) ---")

    for email in grouped["FYI"]:
        print(f" - {email['subject']}")

    # ARCHIVE
    print(f"\n--- ARCHIVE ({len(grouped['ARCHIVE'])} emails skipped) ---")

    print("=" * 50)
    print("=== END DIGEST ===")


# Hardcoded test emails
test_emails = [
    {
        "sender": "OSHA Inspector",
        "subject": "Fall protection deficiency",
        "body": "Missing guardrails found on Level 4 east side. Immediate correction required before work resumes.",
        "triage_category": "URGENT"
    },
    {
        "sender": "Project Architect",
        "subject": "RFI-047 Response",
        "body": "Architect approved revised rebar spacing at Pier 3. Proceed with installation.",
        "triage_category": "ACTION"
    },
    {
        "sender": "Concrete Supplier",
        "subject": "Updated delivery schedule",
        "body": "Thursday concrete pour moved to Friday because of plant maintenance.",
        "triage_category": "ACTION"
    },
    {
        "sender": "Safety Department",
        "subject": "Weekly safety stats",
        "body": "Attached are the February safety statistics and toolbox talk summaries.",
        "triage_category": "FYI"
    },
    {
        "sender": "Marketing",
        "subject": "Industry newsletter",
        "body": "New updates regarding OSHA silica dust regulations.",
        "triage_category": "FYI"
    },
    {
        "sender": "Promotions",
        "subject": "Special discount offer",
        "body": "Limited-time software promotion for construction companies.",
        "triage_category": "ARCHIVE"
    }
]


if __name__ == "__main__":
    print_digest(test_emails)
