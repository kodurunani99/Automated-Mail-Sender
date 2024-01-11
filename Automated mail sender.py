import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, to_email, smtp_server, smtp_port=587):
    # Create the MIME object
    msg = MIMEMultipart()
    msg['From'] = 'kodurunani99@gmail.com' # Replace with your sender email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the email body
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Establish a connection to the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            # Start the TLS connection
            server.starttls()

            # Log in to the email account
            server.login('kodurunani99@gmail.com', 'Replace_this_with_your_app_password')  # Replace with your credentials

            # Send the email
            server.sendmail(msg['From'], to_email, msg.as_string())

        print(f"Email sent successfully to {to_email}")

    except Exception as e:
        print(f"Error sending email: {e}")

# Example usage:
subject = "Test Email"
body = "This is a test email with STARTTLS."
recipient_email = 'kodurunani99@gmail.com'
smtp_server = 'smtp.gmail.com'  # Replace with your SMTP server address
smtp_port = 587  # Replace with the appropriate port (usually 587 for STARTTLS)
to_email = 'kodurunani99@gmail.com'

# Send the email
send_email(subject, body, recipient_email, smtp_server, smtp_port)