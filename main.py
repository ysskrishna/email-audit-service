from core.email_parser import EmailParser

def main():
    print("Email Audit Service Started")

    # # Case1: Email with image attachment + Email without image attachment
    email_threads = ["data/email_with_image_attachment.eml", "data/email_without_image_attachment.eml"]

    # Case2: Email with image attachment
    # email_threads = ["data/email_with_image_attachment.eml"]

    # # Case3: Email without image attachment
    # email_threads = ["data/email_without_image_attachment.eml"]

    employee_domain = "@test.com"

    
    for email_path in email_threads:
        print(f"\n📄 Processing: {email_path}")
        parser = EmailParser(email_path)
        all_msgs = parser.extract_all_messages()
        print(f"🔎 Total messages: {len(all_msgs)}")

        employee_msgs = [
            msg for msg in all_msgs
            if parser.extract_email_data(msg)['sender'].lower().endswith(employee_domain)
        ]

        if not employee_msgs:
            print(f"⚠ No employee messages found in {email_path}.")
            continue

        print(f"👤 Employee messages: {employee_msgs}")
        for idx, msg in enumerate(employee_msgs, 1):
            email_data = parser.extract_email_data(msg)
            print(f"\n📧 Employee Message #{idx}")
            print(f"From: {email_data['from']}")
            print(f"To: {email_data['to']}")
            print(f"Subject: {email_data['subject']}")
            print(f"Date: {email_data['date']}")
            print(f"Body: {email_data['body']}")  # Trimmed

if __name__ == "__main__":
    main()