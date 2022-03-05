import smtplib
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import ssl


def send_mail(
    host_email_adr: str,
    host_email_pw: str,
    email_sender: str,
    email_receiver: str,
    message_subject: str,
    message_content_plain: str,
    message_content_html: str,
    host_ssl_port: int = 465,
) -> None:
    """Sends email with defined content using defined host (e.g. gmail)

    Args:
        host_email_adr (str): email address of host used to send mails
        host_email_pw (str): password of host email address
        email_sender (str):  sender email address
        email_receiver (str): receiver email address. For multiple receipients use "email1@gm.com, email2@gmail.com"
        message_subject (str): message header
        message_content_plain (str): message body as plain text
        message_content_html (str): message body as html 
        host_ssl_port (int, optional): ssl port of host. Defaults to 465.

    Returns:
        None: None
    """
    msg = MIMEMultipart("alternative")
    msg["Subject"] = message_subject
    msg["From"] = email_sender
    msg["To"] = email_receiver
    email_receiver_list = email_receiver.replace(" ", "").split(",")

    content_plain = MIMEText(message_content_plain, "plain")
    content_html = MIMEText(message_content_html, "html")

    msg.attach(content_plain)
    msg.attach(content_html)

    # Create a secure SSL context
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(
        "smtp.gmail.com", host_ssl_port, context=context
    ) as server:
        server.login(host_email_adr, host_email_pw)
        server.sendmail(email_sender, email_receiver_list, msg.as_string())
    print("INFO: email sent")
    return None
