import email
import re
from email import policy
from email.parser import BytesParser
from typing import List


class EmailParser:
    def __init__(self, eml_path: str):
        self.eml_path = eml_path

    def extract_all_messages(self) -> List[email.message.Message]:
        with open(self.eml_path, 'rb') as f:
            msg = BytesParser(policy=policy.default).parse(f)
        return [msg]  # Placeholder: actual threading requires message store

    def extract_email_data(self, msg: email.message.Message) -> dict:
        return {
            "subject": msg.get("Subject"),
            "from": msg.get("From"),
            "to": msg.get("To"),
            "date": msg.get("Date"),
            "message_id": msg.get("Message-ID"),
            "content_type": msg.get_content_type(),
            "body": self._get_body(msg),
            "attachments": self._get_attachments(msg),
            "sender": self._extract_email_address(msg.get("From"))
        }

    def _get_body(self, msg: email.message.Message) -> str:
        text = ""
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain" and not part.get_filename():
                    text = part.get_payload(decode=True).decode(errors="ignore")
                    break
        else:
            text = msg.get_payload(decode=True).decode(errors="ignore")
        return self._strip_quoted_reply(text)

    def _strip_quoted_reply(self, text: str) -> str:
        reply_markers = [
            r"^On .+ wrote:$",        # Common reply line
            r"^From: .*",             # From line
            r"^>+",                   # Quoted lines
            r"^Sent from my .*",      # Mobile signatures
            r"^--$",                  # Signature separator
        ]
        pattern = re.compile("|".join(reply_markers), re.MULTILINE)
        match = pattern.search(text)
        if match:
            text = text[:match.start()]
        return text.strip()

    def _get_attachments(self, msg: email.message.Message) -> List[str]:
        attachments = []
        for part in msg.walk():
            if part.get_content_disposition() == "attachment":
                attachments.append(part.get_filename())
        return attachments

    def _extract_email_address(self, full_address: str) -> str:
        if not full_address:
            return ""
        if '<' in full_address and '>' in full_address:
            return full_address.split('<')[1].split('>')[0]
        return full_address.strip()
