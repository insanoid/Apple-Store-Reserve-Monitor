from discord_webhook import DiscordWebhook
from datetime import datetime

class DiscortAgent():
    def __init__(self, webhook_url):
        self.webhook_url = webhook_url
        self.initial_timer = None
        
    def send_message(self, message):
        if self.initial_timer is None:
            self.initial_timer = datetime.now()
            webhook = DiscordWebhook(url=self.webhook_url,rate_limit_retry=True, content=message)
            response = webhook.execute()
            print("Message sent")
            return response
        else:
            if (datetime.now() - self.initial_timer).min >= 60:
                self.initial_timer = datetime.now()
                webhook = DiscordWebhook(url=self.webhook_url, content=message)
                response = webhook.execute()
                self.initial_timer = datetime.now()
                return response
            else:
                print("Message not sent, time limit not reached")
        return False
    