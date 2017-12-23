from zcan.can_interface import CanInterface


class CanMessageReader(object):
    def __init__(self):
        self.can = CanInterface()

    def process_message(self, message: str):
        print(message)

    def read_messages(self, data):
        while True:
            data["foo"] = self.can.read_message()
