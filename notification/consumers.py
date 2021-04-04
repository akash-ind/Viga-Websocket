from channels.generic.websocket import WebsocketConsumer
import json
from datetime import datetime, timedelta


class NotificationWebConsumer(WebsocketConsumer):
    """
    This recieves connection and send messages etc. Synchronous as
    it does not perform any high end complex tasks.
    """

    def connect(self):
        self.notification = 0
        self.time = datetime.now()
        self.first = True
        self.accept()


    def receive(self, text_data):
        data = json.loads(text_data)
        if data['message'] == 'notify':
            self.notify(text_data)

    def notify(self, event):
        notification = f'New Notification no - {self.notification}'
        self.notification+=1
        if not self.first and datetime.now() - self.time < timedelta(seconds=9):
            # 9 seconds because sometimes javascript and python have a little 
            ##diff
            self.close()
        self.first = False
        self.time = datetime.now()
        self.send(text_data=json.dumps({'notification':notification}))