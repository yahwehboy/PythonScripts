import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Read email addresses from a .txt file
def load_emails(filename):
    with open(filename, 'r') as file:
        # Read lines and strip whitespace, ignore empty lines
        emails = [line.strip() for line in file if line.strip()]
    return emails

# File containing the email addresses
email_file = "emails.txt"
to_addresses = load_emails(email_file)

if not to_addresses:
    print("No email addresses found in the file.")
    exit()

# Email sender and SMTP credentials
from_address = "donotreply=upwork.com@mg.upwork.com"
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_user = "omotayoolaolekan01@gmail.com"
smtp_password = "yxmo imgm ibpt uwfr"  # Use App Password for Gmail

# Create message
msg = MIMEMultipart("alternative")
msg["From"] = from_address
msg["To"] = ", ".join(to_addresses)
msg["Subject"] = "Important Security Alert"

# HTML content
html_body = """
<html>
  <head></head>
  <body>
    <p><strong>Dear User,</strong></p>
    <p>You need to <strong>reset your password immediately</strong> to secure your account.</p>
    <p><button type="submit" style="background-color: yellow;">
      <a href="https://google.com" style="color: blue; font-weight: bold; text-decoration: none;">Reset Password</a>
    </button></p>
    <p>This link will expire in 24 hours.</p>
    <p>Best regards,<br>
       <em>Your IT Team</em>
    </p>
  </body>
</html>
"""

# Attach HTML to email
mime_text = MIMEText(html_body, "html")
msg.attach(mime_text)

# Send email
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Secure the connection
    server.login(smtp_user, smtp_password)
    
    # Send email
    server.sendmail(from_address, to_addresses, msg.as_string())
    print(f"Email sent successfully to {len(to_addresses)} recipient(s): {to_addresses}")

except Exception as e:
    print(f"Failed to send email: {e}")

finally:
    server.quit()