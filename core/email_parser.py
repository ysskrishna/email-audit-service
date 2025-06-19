import email
import re
from email import policy
from email.parser import BytesParser
from typing import List, Optional


class EmailParser:
    def __init__(self, eml_path: str):
        self.eml_path = eml_path
        self.msg = self._load_message()

    def _load_message(self) -> email.message.Message:
        with open(self.eml_path, 'rb') as f:
            return BytesParser(policy=policy.default).parse(f)

    def extract_last_reply(self) -> dict:
        return {
            "subject": self.msg.get("Subject"),
            "from": self.msg.get("From"),
            "to": self.msg.get("To"),
            "date": self.msg.get("Date"),
            "message_id": self.msg.get("Message-ID"),
            "content_type": self.msg.get_content_type(),
            "body": self._get_body(),
            "attachments": self._get_attachments(),
            "sender": self._extract_email_address(self.msg.get("From"))
        }

    def _get_body(self) -> str:
        text = ""
        if self.msg.is_multipart():
            for part in self.msg.walk():
                if part.get_content_type() == "text/plain" and not part.get_filename():
                    text = part.get_payload(decode=True).decode(errors="ignore")
                    break
        else:
            text = self.msg.get_payload(decode=True).decode(errors="ignore")
        return self._strip_quoted_reply(text)

    def _strip_quoted_reply(self, text: str) -> str:
        reply_markers = [
            r"^On .+ wrote:$",
            r"^From: .*",
            r"^>+",
            r"^Sent from my .*",
            r"^--$",
        ]
        pattern = re.compile("|".join(reply_markers), re.MULTILINE | re.IGNORECASE)
        match = pattern.search(text)
        if match:
            text = text[:match.start()]
        return text.strip()

    def _get_attachments(self) -> List[str]:
        attachments = []
        for part in self.msg.walk():
            if part.get_content_disposition() == "attachment":
                attachments.append(part.get_filename())
        return attachments

    def _extract_email_address(self, full_address: Optional[str]) -> str:
        if not full_address:
            return ""
        if '<' in full_address and '>' in full_address:
            return full_address.split('<')[1].split('>')[0]
        return full_address.strip()

    @staticmethod
    def print_email(email):
        print(f"From: {email['from']}")
        print(f"To: {email['to']}")
        print(f"Subject: {email['subject']}")
        print(f"Date: {email['date']}")
        print(f"Content-Type: {email['content_type']}")
        print(f"Body: {email['body']}")
        print(f"Attachments: {email['attachments']}")