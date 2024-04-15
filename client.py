import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email configuration
sender_email = ""
receiver_email = ""
subject = "Test Email"
body = "This is a test email sent from Python."

# Create a multipart message
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

# Add body to email
message.attach(MIMEText(body, "plain"))

# Connect to the SMTP server running on localhost
smtp_server = smtplib.SMTP("localhost", 1025)

# Send the email
smtp_server.sendmail(sender_email, receiver_email, message.as_string())

# Close the connection to the SMTP server
smtp_server.quit()
