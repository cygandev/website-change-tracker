import smtplib
from email.message import EmailMessage
import ssl


def send_mail(
    host_email_adr: str,
    host_email_pw: str,
    email_sender: str,
    email_receiver: str,
    message_subject: str,
    message_content: str,
    host_ssl_port: int = 465,
) -> None:
    """Sends email with defined content using defined host (e.g. gmail)

    Args:
        host_email_adr (str): email address of host used to send mails
        host_email_pw (str): password of host email address
        email_sender (str): receiver email address
        email_receiver (str): sender email address
        message_subject (str): message header
        message_content (str): message body
        host_ssl_port (int, optional): ssl port of host. Defaults to 465.

    Returns:
        None: None
    """
    msg = EmailMessage()
    msg.set_content(message_content)
    msg["Subject"] = message_subject
    msg["From"] = email_sender
    msg["To"] = email_receiver

    # Create a secure SSL context
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(
        "smtp.gmail.com", host_ssl_port, context=context
    ) as server:
        server.login(host_email_adr, host_email_pw)
        server.send_message(msg)
    print("INFO: email sent")
    return None
