import os

from utils.handle_content import (
    read_page_content,
    request_page_content,
    write_page_content,
)
from utils.send_mail import send_mail

URL = os.environ.get("URL")
FILE_PATH = os.environ.get("FILE_PATH", "./website_content.txt")

GMAIL_ADR = os.environ.get("EMAIL")
GMAIL_PW = os.environ.get("PW_GMAIL")
PORT = os.environ.get("SSL_PORT", 465)
SMTP_SERVER = os.environ.get("SMTP_SERVER", "smtp.gmail.com")
EMAIL_SENDER = os.environ.get("EMAIL_SENDER", GMAIL_ADR)
EMAIL_RECEIVER = os.environ.get("EMAIL_RECEIVER", GMAIL_ADR)

if __name__ == "__main__":
    new_page_content = request_page_content(URL)
    try:
        old_page_content = read_page_content(FILE_PATH)
        if old_page_content == new_page_content:
            print("INFO: Webpage scraped, no changes detected")
        else:
            msg_subject = "ALERT - WEBSITE CHANGE DETECTED"
            msg_content = f"A change on the webpage {URL} was detected \
            please visit page."
            send_mail(
                GMAIL_ADR,
                GMAIL_PW,
                GMAIL_ADR,
                GMAIL_ADR,
                message_subject=msg_subject,
                message_content=msg_content,
            )
            print(f"INFO: Change detected, email to {EMAIL_RECEIVER} sent...")
    except FileNotFoundError:
        print("INFO: No file found, initiating...")
    finally:
        write_page_content(FILE_PATH, new_page_content)
        print("INFO: Successfully Written new page content to disk")
