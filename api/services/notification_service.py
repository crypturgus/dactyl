from django.conf import settings
from django.contrib.auth import get_user_model
from mailjet_rest import Client

User = get_user_model()


class NotificationService:
    def send_register_notification(self, user):
        self.send_email(user)

    def send_email(self, user):
        # send email to user
        api_key = settings.MAILJET_API_KEY

        api_secret = settings.MAILJET_SECRET
        mailjet = Client(auth=(api_key, api_secret), version="v3.1")
        data = {
            "Messages": [
                {
                    "From": {
                        "Email": "dactyl-dev@proton.me",
                    },
                    "To": [
                        {
                            "Email": "dactyl-dev@proton.me",
                        }
                    ],
                    "Subject": "Test Register Email",
                    "TextPart": "Dear passenger 1, welcome to Mailjet! May the delivery force be with you!",
                    "HTMLPart": "<h3>Dear passenger 1, welcome to Mailjet!</h3><br />May the delivery force be with you!",
                }
            ]
        }
        result = mailjet.send.create(data=data)
        print(result.status_code)
        print(result.json())
