import serial
import logging
from zcan.exception import ZCanBaseException
from zcan.mapping import mapping
from zcan.util import get_logger


class Message(object):
    def __init__(self, type: str, id: str, length: int, data, raw=None):
        self.type = type
        self.id = id
        self.length = length
        self.data = data
        self.raw = raw

    def __str__(self):
        return "type:{} id:{} length:{} data:{}".format(self.type, self.id, self.length, self.data)

    def print_full_repr(self):
        return "type:{} id:{} length:{} data:{} (raw: {})".format(self.type, self.id, self.length, self.data, self.raw)

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
        try:
            message_mapping = mapping[message.id]
        except KeyError:
            return None

        name = message_mapping["name"]
        unit = message_mapping["unit"]
        transform_function = message_mapping["transformation"]
        try:
            value = transform_function(message.data)
        except Exception as e:
            raise RuntimeError("Could not transform data {} to value for {}, error: {}".format(message.data, name, e))

        return Measurement(name, message.id, value, unit)

    def __str__(self):
        return "name: {} id:{} value:{} unit:{}".format(self.name, self.id, self.value, self.unit)

    def __eq__(self, other):
        if self.name == other.name and self.id == other.id and self.value == other.value and self.unit == other.unit:
            return True
        else:
            return False


class CanBus(object):
    def __init__(self):
        self.logger = get_logger("CanBusReader")
        self.can = CanBusInterface()

    def read_messages(self, measurements, unknown_messages):
        self.can.open()
        try:
            while True:
                try:
                    message = self.can.read_message()
                    if message:
                        self.logger.debug(message)
                        measurement = Measurement.from_message(message)
                        if measurement:
                            measurements[measurement.name] = measurement
                        else:
                            unknown_messages[message.id] = message
                except Exception as e:
                    self.logger.exception(e)
        finally:
            self.can.close()

    def print_messages(self, all: bool):
        self.can.open()
        try:
            while True:
                try:
                    message = self.can.read_message()
                    if message:
                        try:
                            mapping[message.id]
                            if all:
                                print(message.print_full_repr())
                        except KeyError:
                            print(message.print_full_repr())
                except Exception as e:
                    print(e)
        finally:
            self.can.close()

    def write(self, payload):
        self.can.open()

        try:
            if isinstance(payload, str):
                self.can.write_message_string(payload)
            else:
                self.can.write_message_bytes(payload)
        finally:
            self.can.close()

    def write_messages(self, payloads: list):
        self.can.open()
        try:
            for payload in payloads:
                if isinstance(payload, str):
                    self.can.write_message_string(payload)
                else:
                    self.can.write_message_bytes(payload)
        finally:
            self.can.close()

    def get_error_state(self):
        self.can.open()
        try:
            print(self.can.get_error_state())
        finally:
            self.can.close()


class CanBusInterface(object):
    def __init__(self, device="/dev/ttyACM0"):
        self.logger = get_logger("CanBusInterface")
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

            type = frame[0:1].decode("ascii")
            assert type.lower() in ["t", "r"], "message type must be T or R, not '{}'".format(type)

            id = frame[1:9].decode("ascii")
            length = int(frame[9:10], 16)

            index = 10
            data = []

            for item in range(0, length):
                data.append(int(frame[index:index + 2], 16))
                index += 2

            return Message(type, id, length, data, frame)
        except Exception as e:
            print("Could not parse can frame '{}', error was: {}".format(frame, e))

    def read(self):
        return self.connection.read_until(b'\r')

    def read_message(self):
        """
        read until stop character is found or timeout occurs
        :return: one line as bytestring
        """
        frame = self.read()
        self.logger.debug(frame)
        return self._to_can_message(frame)

    def get_error_state(self):
        self.connection.write(b"F\r")
        return self.read()

    def write_message_string(self, payload: str):
        message = bytearray("{}\r".format(payload), encoding="ascii")
        print("Going to send: {}".format(message))
        self.connection.write(message)

    def write_message_bytes(self, payload: bytes):
        print("Going to send bytes: {}".format(payload))
        self.connection.write(payload)


if __name__ == "__main__":
    interface = CanBusInterface()
    interface.open()
    while True:
        print(interface.read_message())
