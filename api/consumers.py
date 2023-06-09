import json
from channels.generic.websocket import WebsocketConsumer


class VacancyConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()

    def disconnect(self, code):
        pass

    def receive(self, text_data=None, bytes_data=None):
        self.send(text_data=json.dumps(text_data))
