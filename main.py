
def main():
    print("Email Audit Service Started")

    # # Case1: Email with image attachment + Email without image attachment
    # email_threads = ["data/email_with_image_attachment.eml", "data/email_without_image_attachment.eml"]

    # Case2: Email with image attachment
    email_threads = ["data/email_with_image_attachment.eml"]

    # # Case3: Email without image attachment
    # email_threads = ["data/email_without_image_attachment.eml"]

    print(f"Email threads: {email_threads}")


if __name__ == "__main__":
    main()