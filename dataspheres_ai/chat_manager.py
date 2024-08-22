import asyncio

class ChatManager:
    def __init__(self, event_stream):
        self.event_stream = event_stream
        self.chats = {}

    def create_chat(self, chat_id):
        if chat_id not in self.chats:
            self.chats[chat_id] = []

    def add_message(self, chat_id, message):
        if chat_id in self.chats:
            self.chats[chat_id].append(message)
            asyncio.create_task(self.event_stream.send_event({'chat_id': chat_id, 'message': message}))
        else:
            self.chats[chat_id] = [message]
            asyncio.create_task(self.event_stream.send_event({'chat_id': chat_id, 'message': message}))

    def get_chat_history(self, chat_id):
        return self.chats.get(chat_id, [])
