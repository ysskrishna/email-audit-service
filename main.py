from core.email_parser import EmailParser
from ruleengine.engine import RuleEngine
from core.enums import RuleEnum

import argparse

def main():
    parser = argparse.ArgumentParser(description="Run Email Audit Service")
    parser.add_argument('--emails', nargs='+', required=True, help='Paths to email thread .eml files')
    parser.add_argument('--employee-domain', default='@test.com', help='Employee email domain')
    parser.add_argument('--rules', nargs='+', default=['GREETING', 'CLARITY', 'GRAMMAR', 'TONE'], help='Rules to apply')
    
    args = parser.parse_args()

    print(f"🔎 Email threads: {args.emails}")
    print(f"🔎 Employee domain: {args.employee_domain}")
    print(f"🔎 Rules: {args.rules}")

    email_threads = args.emails
    employee_domain = args.employee_domain
    selected_rules = [RuleEnum[rule] for rule in args.rules]

    total_email_threads_counter = len(email_threads)
    valid_employee_reply_counter = 0
    invalid_email_counter = 0

    rule_engine = RuleEngine()
    
    for email_path in email_threads:
        print(f"\n📄 Processing: {email_path}")
        parser = EmailParser(email_path)

        last_reply = parser.extract_last_reply()
        EmailParser.print_email(email_path, last_reply)    

        if not last_reply.sender.lower().endswith(employee_domain):
            print(f"⚠ Last reply is not from the employee")
            invalid_email_counter += 1
            continue
        
        if not len(last_reply.attachments) > 0:
            print(f"⚠ Email does not have attachment")
            invalid_email_counter += 1
            continue
        
        valid_employee_reply_counter += 1
        result = rule_engine.run(last_reply, selected_rules)
        RuleEngine.print_output(email_path, result)

    print(f"🔎 Total email threads: {total_email_threads_counter}")
    print(f"🔎 Valid employee reply: {valid_employee_reply_counter}")
    print(f"🔎 Invalid email threads: {invalid_email_counter}")

if __name__ == "__main__":
    main()