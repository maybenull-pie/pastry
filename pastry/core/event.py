class Event(object):
    def __init__(self, body: dict, message_type: str):
        self.body = body
        self.message_type = message_type

class ISqsHappend(Event):
    def __init__(self, body: dict):
        super().__init__(body, 'Message.From.SomeWhere.ISqsHappened')
    