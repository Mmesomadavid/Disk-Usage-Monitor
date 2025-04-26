# Disk Usage Monitor

A Python script to monitor disk usage and send email alerts when the usage exceeds a specified threshold.

## Features

- Monitors disk usage of a specified path.
- Sends an email alert if disk usage exceeds the defined threshold.
- Configurable settings for threshold percentage, email credentials, and SMTP server.

## Requirements

- Python 3.x
- Required Python libraries:
  - `shutil` (built-in)
  - `smtplib` (built-in)
  - `email` (built-in)

## Installation

1. Clone this repository or download the script file.
2. Install Python 3.x if not already installed.
3. Ensure you have an email account with SMTP access (e.g., Gmail).

## Configuration

Edit the `monitor_disk_usage.py` file to configure the following settings:

- `THRESHOLD_PERCENT`: The disk usage percentage at which an alert is triggered (default: 80%).
- `ALERT_EMAIL`: The recipient email address for alerts.
- `SMTP_SERVER`: The SMTP server address (default: `smtp.gmail.com` for Gmail).
- `SMTP_PORT`: The SMTP server port (default: 587).
- `SMTP_USER`: Your email address for sending alerts.
- `SMTP_PASS`: Your email password or app-specific password.

**Note:** For Gmail, you may need to generate an [App Password](https://support.google.com/accounts/answer/185833?hl=en) to use with this script.

## Usage

1. Open a terminal or command prompt.
2. Run the script using Python:

   ```bash
   python monitor_disk_usage.py
   
