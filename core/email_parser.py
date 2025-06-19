import email
from email import policy
from email.parser import BytesParser
from typing import List, Any

class EmailParser:
    def __init__(self, eml_path: str):
        self.eml_path = eml_path

    def extract_all_messages(self) -> List[email.message.Message]:
        with open(self.eml_path, 'rb') as f:
            msg = BytesParser(policy=policy.default).parse(f)
        # Flattening the message thread
        messages = [msg]
        while msg.get('In-Reply-To') or msg.get('References'):
            # In a real thread parser, you'd look up the referenced message
            break  # Placeholder: Only current message
        return messages

    def extract_email_data(self, msg: email.message.Message) -> dict:
        data = {
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
        return data

    def _get_body(self, msg: email.message.Message) -> str:
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    return part.get_payload(decode=True).decode(errors="ignore")
        else:
            return msg.get_payload(decode=True).decode(errors="ignore")
        return ""

    def _get_attachments(self, msg: email.message.Message) -> List[str]:
        attachments = []
        for part in msg.walk():
            if part.get_content_disposition() == "attachment":
                attachments.append(part.get_filename())
        return attachments

    def _extract_email_address(self, full_address: str) -> str:
        if not full_address:
            return ""
        # Example: 'siva <siva@test.com>' -> 'siva@test.com'
        if '<' in full_address and '>' in full_address:
            return full_address.split('<')[1].split('>')[0]
        return full_address.strip()
