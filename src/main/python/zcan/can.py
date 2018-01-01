import serial
from zcan.mapping import mapping


class Message(object):
    def __init__(self, type: str, id: str, length: int, data):
        self.type = type
        self.id = id
        self.length = length
        self.data = data

    def __str__(self):
        return "type:{} id:{} length:{} data:{}".format(self.type, self.id, self.length, self.data)

    def __eq__(self, other):
        if self.type == other.type and self.id == other.id and self.length == other.length and self.data == other.data:
            return True
        else:
            return False


class Measurement(object):
    def __init__(self, name: str, id: str, value, unit: str):
        self.name = name
        self.id = id
        self.value = value
        self.unit = unit

    @staticmethod
    def from_message(message: Message):
        transform_function = mapping[message.id]["transformation"]
        name = mapping[message.id]["name"]
        unit = mapping[message.id]["unit"]

        value = transform_function(message.data)
        return Measurement(name, message.id, value, unit)

    def __str__(self):
        return "name: {} id:{} value:{} unit:{}".format(self.name, self.id, self.value, self.unit)

    def __eq__(self, other):
        if self.name == other.name and self.id == other.id and self.value == other.value and self.unit == other.unit:
            return True
        else:
            return False


class CanBusReader(object):
    def __init__(self):
        self.can = CanBusInterface()

    def read_messages(self, data):
        self.can.open()
        try:
            while True:
                message = self.can.read_message()
                measurement = Measurement.from_message(message)
                data[measurement.name] = measurement
        finally:
            self.can.close()


class CanBusInterface(object):
    def __init__(self, device="/dev/ttyACM0"):
        self.connection = serial.serial_for_url(device, do_not_open=True)
        self.connection.baudrate = 115200

    def close(self):
        """
        tell SUBtin to close the CAN bus connection and close serial connection
        """
        self.connection.write(b'C\r')
        self.connection.close()

    def open(self):
        """
        open serial connection and tell USBtin to use a CAN baud rate of 50k (S2)
        """
        self.connection.open()
        self.connection.write(b'S2\r')
        self.connection.write(b'O\r')

    @staticmethod
    def _to_can_message(frame: bytes) -> Message:
        try:
            frame = frame.strip(b'\x07')

            type = frame[0:1].decode("utf-8")
            assert type.lower() in ["t", "r"], "message type must be T or R, not '{}'".format(type)

            id = frame[1:9].decode("utf-8")
            length = int(frame[9:10], 16)

            index = 10
            data = []

            for item in range(0, length):
                data.append(int(frame[index:index + 2], 16))
                index += 2

            return Message(type, id, length, data)
        except Exception as e:
            print("Could not parse can frame '{}', error was: {}".format(frame, e))

    def read_message(self):
        """
        read until stop character is found or timeout occurs
        :return: one line as bytestring
        """
        frame = self.connection.read_until(b'\r')
        return self._to_can_message(frame)


if __name__ == "__main__":
    interface = CanBusInterface()
    interface.open()
    while True:
        print(interface.read_message())
