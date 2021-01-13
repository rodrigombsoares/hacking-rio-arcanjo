from twilio.rest import Client


class BotUtils():
    def __init__(self):
        self.account_sid = 'ACaa145834a76601dd72e47961f81272f8'
        self.auth_token = '2454f825010aaa67be9512bbac4ca047'
        self.bot_phone = 'whatsapp:+14155238886'
        self.client = Client(self.account_sid, self.auth_token)


    def send_message(self, body, to, media):
        if media:
            message = self.client.messages.create(
                from_=self.bot_phone,
                body=body,
                to=to,
                media_url=[media]
            )
        else:
            message = self.client.messages.create(
                from_=self.bot_phone,
                body=body,
                to=to
            )