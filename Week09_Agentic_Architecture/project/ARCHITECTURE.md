# Architecture — Email Communication Agent

## Overview

This project is an AI-assisted email communication agent that reads
emails from an inbox, classifies them by urgency, generates summaries,
creates draft replies, and optionally sends approved responses.

## Components

### Reader
- Responsibility: Fetch emails from IMAP inbox
- Input: Email account credentials
- Output: Email dictionaries
- File: reader.py

### Digest
- Responsibility: Create a morning summary of emails
- Input: Email list
- Output: Formatted digest
- File: digest.py

### Templates
- Responsibility: Generate professional email drafts
- Input: Email content and category
- Output: Draft response
- File: templates.py

### Agent
- Responsibility: Orchestrates the workflow
- Input: Emails from reader.py
- Output: Drafts and sent emails
- File: agent.py

## Data Flow Diagram

IMAP Inbox
    |
    v
+----------+
| reader.py|
+----------+
    |
    v
+----------+
| classifier|
+----------+
    |
    v
+----------+
|digest.py |
+----------+
    |
    v
+------------+
|templates.py|
+------------+
    |
    v
+----------+
| agent.py |
+----------+
    |
    v
SMTP Server

## Design Decisions

### Decision 1: Human-in-the-loop approval

Context:
Sending emails automatically can cause mistakes.

Consequences:
Users must approve each email before sending, improving safety.

### Decision 2: Rule-based triage

Context:
Simple keyword rules are easy to understand and maintain.

Consequences:
Fast classification but may be less accurate than advanced AI models.

## Error Handling

- IMAP connection failures are caught and reported.
- Missing environment variables stop execution safely.
- SMTP errors are displayed to the user.
- Invalid recipients trigger warnings.

## Future Extensions

- Telegram integration
- Slack integration
- Persistent memory
- Attachment summarization
- Scheduled execution
