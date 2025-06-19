from core.email_parser import EmailParser

def main():
    print("Email Audit Service Started")

    # # Case1: Employee reply Email with image attachment + Employee reply Email without image attachment
    # email_threads = ["data/employee_reply_email_with_image_attachment.eml", "data/employee_reply_email_without_image_attachment.eml"]

    # Case2: Employee reply Email with image attachment
    email_threads = ["data/employee_reply_email_with_image_attachment.eml"]

    # # Case3: Employee reply Email without image attachment
    # email_threads = ["data/employee_reply_email_without_image_attachment.eml"]

    # Case4: Non employee reply email
    # email_threads = ["data/non_employee_reply_email.eml"]

    employee_domain = "@test.com"
    total_email_threads_counter = len(email_threads)
    valid_employee_reply_counter = 0
    invalid_email_counter = 0


    
    for email_path in email_threads:
        print(f"\n📄 Processing: {email_path}")
        parser = EmailParser(email_path)

        last_reply = parser.extract_last_reply()
        # EmailParser.print_email(last_reply)    

        # Check if the last reply is from the employee
        if not last_reply['sender'].lower().endswith(employee_domain):
            print(f"⚠ Last reply is not from the employee")
            invalid_email_counter += 1
            continue
        
        # Add a condition to check if the email has attachment ?
        if not len(last_reply['attachments']) > 0:
            print(f"⚠ Email does not have attachment")
            invalid_email_counter += 1
            continue
        
        valid_employee_reply_counter += 1

    print(f"🔎 Total email threads: {total_email_threads_counter}")
    print(f"🔎 Valid employee reply: {valid_employee_reply_counter}")
    print(f"🔎 Invalid email threads: {invalid_email_counter}")

        


if __name__ == "__main__":
    main()