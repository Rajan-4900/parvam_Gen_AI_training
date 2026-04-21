import os
import smtplib
import secrets
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def _load_env(env_path='.env'):
    """Load simple KEY=VALUE pairs from a .env file located next to this module.
    Returns a dict with values (falls back to real environment variables).
    """
    values = {}
    try:
        base = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(base, env_path)
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith('#'):
                        continue
                    if '=' in line:
                        k, v = line.split('=', 1)
                        values[k.strip()] = v.strip().strip('"').strip("'")
    except Exception:
        pass

    # fallback to environment variables
    for k in ('EMAIL', 'APP_PASSWORD'):
        if k not in values and os.getenv(k):
            values[k] = os.getenv(k)
    return values


def send_reset_email(recipient_email):
    """Send a password reset email to `recipient_email`.

    Reads `EMAIL` and `APP_PASSWORD` from a local `.env` next to this file or
    from the environment. Returns the generated token string on success,
    or None on failure.
    """
    cfg = _load_env()
    sender_email = cfg.get('EMAIL')
    app_password = cfg.get('APP_PASSWORD')

    if not sender_email or not app_password:
        print('EMAIL or APP_PASSWORD not configured in .env or environment')
        return None

    token = secrets.token_urlsafe(32)
    reset_link = f"http://localhost:5000/reset_password/{token}"

    msg = MIMEMultipart('alternative')
    msg['Subject'] = 'Password Reset Request'
    msg['From'] = sender_email
    msg['To'] = recipient_email

    text = (
        'You requested a password reset. Open this link to reset your password:\n\n'
        + reset_link
        + '\n\nIf you did not request this, ignore.'
    )

    html = (
        '<html><body>'
        '<p>You requested a password reset. Click the link below to reset your password:</p>'
        f'<p><a href="{reset_link}">Reset your password</a></p>'
        '<p>If you did not request this, ignore this message.</p>'
        '</body></html>'
    )

    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    msg.attach(part1)
    msg.attach(part2)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587, timeout=30)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(sender_email, app_password)
        server.send_message(msg)
        server.quit()
        print('Password reset email sent to', recipient_email)
        return token
    except Exception as e:
        print('Failed to send reset email:', e)
        return None


if __name__ == '__main__':
    recipient = input("Enter the recipient's email address: ")
    token = send_reset_email(recipient)
    if token:
        print('Reset token generated:', token)
