import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Define the email parameters
from_address = "donotreply=upwork.com@mg.upwork.com"
to_addresses = ["andersonclarkson41@gmail.com", "omotayoolaolekan01@outlook.com"]

# SMTP server details (replace with your actual SMTP server)
smtp_server = "smtp.gmail.com"  # Example: Mailtrap for testing
smtp_port = 587
smtp_user = "omotayoolaolekan01@gmail.com"      # Replace with your SMTP username
smtp_password = "yxmo imgm ibpt uwfr"  # Replace with your SMTP password

# Create a MIME-based message to support HTML
msg = MIMEMultipart("alternative")
msg["From"] = from_address
msg["To"] = ", ".join(to_addresses)
msg["Subject"] = "Important Security Alert"

# HTML content of the email
html_body = """
<html>
  <head></head>
  <body>
    <p><strong>Dear User,</strong></p>
    <p>You need to <strong>reset your password immediately</strong> to secure your account.</p>
    <p><button type="submit" style="background-color: yellow;">
      <a href="https://google.com" style="color: blue; font-weight: bold; text-decoration: none;"></a></button>
    </p>
    <p>This link will expire in 24 hours.</p>
    <p>Best regards,<br>
       <em>Your IT Team</em>
    </p>
  </body>
</html>
"""

# Convert the HTML into a MIMEText object
mime_text = MIMEText(html_body, "html")

# Attach the HTML part to the message
msg.attach(mime_text)

# Connect to the SMTP server and send the email
try:
    # Initialize connection to the SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)

    # Upgrade the connection to secure using STARTTLS
    server.starttls()

    # Login to the SMTP server
    server.login(smtp_user, smtp_password)

    # Send the email
    server.sendmail(from_address, to_addresses, msg.as_string())

    # Print success message
    print("HTML email sent successfully!")

except Exception as e:
    # Print error message if something goes wrong
    print(f"Failed to send email: {e}")

finally:
    # Close the connection
    server.quit()