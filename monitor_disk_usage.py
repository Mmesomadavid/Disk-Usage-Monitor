import shutil
import smtplib
from email.mime.text import MIMEText

# Settings
THRESHOLD_PERCENT = 80  # Alert if disk usage is over 80%
ALERT_EMAIL = "chukwunoyelummesoma1@gmail.com"  # Your email here
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USER = "primehealthnig@gmail.com"  # Your SMTP email
SMTP_PASS = "lutylyapaceulfln"     # Your SMTP password (or App password)

def check_disk_usage(path):
    total, used, free = shutil.disk_usage(path)
    percent_used = (used / total) * 100
    return percent_used

def send_alert_email(usage_percent):
    subject = "Disk Usage Alert!"
    body = f"Warning! Disk usage is at {usage_percent:.2f}%"
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = SMTP_USER
    msg['To'] = ALERT_EMAIL

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USER, SMTP_PASS)
        server.send_message(msg)
        server.quit()
        print(f"Alert email sent to {ALERT_EMAIL} 🚀")
    except Exception as e:
        print(f"Failed to send email: {e}")

def main():
    path = "/"  # Root partition
    usage = check_disk_usage(path)
    print(f"Current Disk Usage: {usage:.2f}%")
    if usage > THRESHOLD_PERCENT:
        send_alert_email(usage)

if __name__ == "__main__":
    main()
