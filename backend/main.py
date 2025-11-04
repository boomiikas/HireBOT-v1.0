from fastapi import FastAPI
from dotenv import load_dotenv
import os
from mailjet_rest import Client

load_dotenv()

MAILJET_API_KEY = os.getenv("MAILJET_API_KEY")
MAILJET_SECRET_KEY = os.getenv("MAILJET_SECRET_KEY")
SENDER_EMAIL = os.getenv("SENDER_EMAIL")

app = FastAPI()

@app.post("/api/send-email")
def send_email(to: str, subject: str, message: str):
    mailjet = Client(auth=(MAILJET_API_KEY, MAILJET_SECRET_KEY), version='v3.1')
    data = {
        'Messages': [
            {
                "From": {
                    "Email": SENDER_EMAIL,
                    "Name": "HireBot"
                },
                "To": [
                    {
                        "Email": to,
                        "Name": "Recipient"
                    }
                ],
                "Subject": subject,
                "TextPart": message,
            }
        ]
    }
    result = mailjet.send.create(data=data)
    return result.status_code, result.json()
