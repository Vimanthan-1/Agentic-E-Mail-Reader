import imaplib
import email
import os
from crewai.tools import BaseTool
from typing import Any, Type
from pydantic import BaseModel

class NoArgs(BaseModel):
    pass

class EmailReaderTool(BaseTool):
    name: str = "Email Reader Tool"
    description: str = "Reads last 2 unread emails from inbox"
    args_schema: Type[BaseModel] = NoArgs

    def _run(self) -> Any:
        mail = imaplib.IMAP4_SSL(os.getenv("IMAP_SERVER"))
        mail.login(os.getenv("EMAIL_ADDRESS"), os.getenv("EMAIL_PASSWORD"))
        mail.select("inbox")

        _, messages = mail.search(None, "UNSEEN")
        email_ids = messages[0].split()[:2]

        emails = []

        for e_id in email_ids:
            _, msg_data = mail.fetch(e_id, "(RFC822)")
            msg = email.message_from_bytes(msg_data[0][1])

            emails.append({
                "from": msg["From"],
                "subject": msg["Subject"]
            })

        mail.logout()
        return emails
