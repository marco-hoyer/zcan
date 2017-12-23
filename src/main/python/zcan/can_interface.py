import serial


class CanInterface(object):
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

    def read_message(self):
        """
        read until stop character is found or timeout occurs
        :return: one line as bytestring
        """
        return self.connection.read_until(b'\r')


if __name__ == "__main__":
    interface = CanInterface()
    interface.open()
    interface.read_message()
