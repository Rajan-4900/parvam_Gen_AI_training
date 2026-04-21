import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

def send_email():
    print("=== Send Email ===")

    # Load .env
    load_dotenv()

    sender_email = os.getenv("EMAIL")
    app_password = os.getenv("APP_PASSWORD")

    if not sender_email or not app_password:
        print("❌ EMAIL or APP_PASSWORD not found in .env")
        return

    receiver_email = input("Enter recipient email: ").strip()
    subject = input("Enter subject: ").strip()

    print("Enter email body (end with single '.' line):")
    lines = []
    while True:
        line = input()
        if line == ".":
            break
        lines.append(line)

    body = "\n".join(lines)

    # Create message
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, app_password)

        server.send_message(msg)
        server.quit()

        print("✅ Email sent successfully!")

    except Exception as e:
        print("❌ Error sending email:", e)


if __name__ == "__main__":
    send_email()