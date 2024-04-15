import asyncore
import smtplib
from smtpd import SMTPServer


class MySMTPServer(SMTPServer):
    def process_message(self, peer, mailfrom, rcpttos, data, **kwargs):
        print(f"Received message from: {mailfrom}")
        print(f"Recipient list: {rcpttos}")
        print("Message data:")
        print(data)

        # Create a new SMTP session to forward the email
        with smtplib.SMTP("smtp.mail.me.com", 587) as external_smtp:
            external_smtp.starttls()
            # Replace with your credentials
            external_smtp.login(
                "EMAIL",
                "APP_SPECIFIC_PASSWORD",
            )
            external_smtp.sendmail(mailfrom, rcpttos, data)


def run_smtp_server():
    server = MySMTPServer(("localhost", 1025), None)
    print("SMTP server running on localhost:1025...")
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        server.close()


if __name__ == "__main__":
    run_smtp_server()
