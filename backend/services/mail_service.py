import os
from mailjet_rest import Client
from dotenv import load_dotenv

# Explicit path to .env (important for Docker)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_PATH = os.path.join(BASE_DIR, ".env")

load_dotenv(ENV_PATH)

MAILJET_API_KEY = os.getenv("MAILJET_API_KEY")
MAILJET_API_SECRET = os.getenv("MAILJET_API_SECRET")
MAIL_SENDER_EMAIL = os.getenv("MAIL_SENDER_EMAIL")
MAIL_SENDER_NAME = os.getenv("MAIL_SENDER_NAME")

print("Loaded MAIL_SENDER_EMAIL:", MAIL_SENDER_EMAIL)
print("Loaded MAILJET_API_KEY:", MAILJET_API_KEY)

mailjet = Client(auth=(MAILJET_API_KEY, MAILJET_API_SECRET), version='v3.1')
mailjet.api_url = 'https://api.mailjet.com/v3.1'

def send_email(to, subject, message):
    data = {
        'Messages': [
            {
                "From": {
                    "Email": MAIL_SENDER_EMAIL,
                    "Name": MAIL_SENDER_NAME
                },
                "To": [
                    {
                        "Email": to,
                        "Name": "Recipient"
                    }
                ],
                "Subject": subject,
                "TextPart": message
            }
        ]
    }
    result = mailjet.send.create(data=data)
    return result.status_code, result.json()
