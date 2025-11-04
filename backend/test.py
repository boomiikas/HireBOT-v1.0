from mailjet_rest import Client

api_key = 'f20178ce348b30534dfcb96fa0236c2b'
api_secret = '47d6a22e508094b549d6cbce8466e8f'

mailjet = Client(auth=(api_key, api_secret), version='v3.1')

data = {
    'Messages': [
        {
            "From": {
                "Email": "boomika2007@gmail.com",
                "Name": "Boomika"
            },
            "To": [
                {
                    "Email": "boomikas.cs24@bitsathy.ac.in",
                    "Name": "Boomika"
                }
            ],
            "Subject": "Test Mailjet email",
            "TextPart": "This is a test message from Mailjet API",
        }
    ]
}

result = mailjet.send.create(data=data)
print("Status code:", result.status_code)
print("Response:", result.json())
