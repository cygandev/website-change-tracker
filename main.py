import os

from utils.handle_content import (
    read_page_content,
    request_page_content,
    request_page_content_hide_ip,
    write_page_content,
)
from utils.send_mail import send_mail

URL = os.environ.get("URL")
WEBPAGE_CONTENT_PATH = os.environ.get(
    "WEBPAGE_CONTENT_PATH", "./files/website_content.txt"
)
HTML_MESSAGE_PATH = os.environ.get(
    "HTML_MESSAGE_PATH", "./files/msg_content.html"
)

GMAIL_ADR = os.environ.get("EMAIL")
GMAIL_PW = os.environ.get("PW_GMAIL")
PORT = int(os.environ.get("SSL_PORT", 465))
SMTP_SERVER = os.environ.get("SMTP_SERVER", "smtp.gmail.com")
EMAIL_SENDER = os.environ.get("EMAIL_SENDER", GMAIL_ADR)
EMAIL_RECEIVER = os.environ.get("EMAIL_RECEIVER", GMAIL_ADR)
USE_PROXY = int(os.environ.get("USE_PROXY", 0))

request_headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) \
        AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/92.0.4515.107 Safari/537.36"
}

if __name__ == "__main__":
    if USE_PROXY:
        new_page_content = request_page_content_hide_ip(
            URL, headers=request_headers
        )
    else:
        new_page_content = request_page_content(URL, headers=request_headers)
    try:
        old_page_content = read_page_content(WEBPAGE_CONTENT_PATH)
        if old_page_content == new_page_content:
            print("INFO: Webpage scraped, no changes detected")
        else:
            msg_subject = "ALERT - WEBSITE CHANGE DETECTED"
            msg_content_plain = f"A change on the webpage {URL} was detected \
            please visit page."
            with open(HTML_MESSAGE_PATH, "r") as f:
                msg_content_html = f.read().format(OBSERVED_URL=URL)

            send_mail(
                GMAIL_ADR,
                GMAIL_PW,
                EMAIL_SENDER,
                EMAIL_RECEIVER,
                message_subject=msg_subject,
                message_content_plain=msg_content_plain,
                message_content_html=msg_content_html,
            )
            print(f"INFO: Change detected, email to {EMAIL_RECEIVER} sent...")
    except FileNotFoundError:
        print("INFO: No file found, initiating...")
    finally:
        write_page_content(WEBPAGE_CONTENT_PATH, new_page_content)
        print("INFO: Successfully Written new page content to disk")
