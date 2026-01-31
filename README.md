# 📧 Agentic Email Reader

An **agent-based email reader system** built using LLM agents that can automatically read unread emails, extract key information, understand intent, and optionally draft replies.

This project demonstrates how to build an **agentic workflow** where multiple AI agents collaborate to handle real-world tasks like email processing.

---

## 🚀 Features

- Connects to your email inbox (Gmail / IMAP)
- Reads **unread emails**
- Extracts:
  - Sender
  - Subject
  - Body
- Analyzes **email intent**
- Categorizes emails (important, spam, job, meeting, etc.)
- Can generate **draft replies**
- Fully agent-based architecture

---

## 🧠 Architecture (How It Works)

The system uses multiple agents, each with a specific role.

### Agents Used

#### 1. Email Reader Agent
- Fetches unread emails
- Extracts raw content

#### 2. Intent Analyzer Agent
- Understands what the email is about
- Classifies intent (query, request, spam, notification)

#### 3. Response Generator Agent (optional)
- Drafts a reply based on intent
- Does NOT auto-send (human-in-the-loop)

---

## 🗂️ Project Structure

```bash
agentic-email-reader/
│
├── main.py                  # Entry point
├── agents.py                # All agent definitions
├── tools.py                 # Email tools (Gmail / IMAP)
├── .env                     # API keys (not committed)
├── requirements.txt
└── README.md
