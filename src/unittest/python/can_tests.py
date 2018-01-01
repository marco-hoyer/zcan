from unittest2 import TestCase
from zcan.can import CanBusInterface, Message


class CanTests(TestCase):
    def test_to_can_message_converts_extended_transmit_frame_with_one_byte(self):
        result = CanBusInterface._to_can_message(b'T001D804111D\r')
        print(result)
        self.assertEqual(result, Message("T", "001D8041", 1, [29]))

    def test_to_can_message_converts_extended_transmit_frame_with_two_bytes(self):
        result = CanBusInterface._to_can_message(b'T001E804123B05\r')
        self.assertEqual(result, Message("T", "001E8041", 2, [59, 5]))

    def test_to_can_message_converts_extended_transmit_frame_with_four_bytes(self):
        result = CanBusInterface._to_can_message(b'T00144041422180200\r')
        self.assertEqual(result, Message("T", "00144041", 4, [34, 24, 2, 0]))

    def test_to_can_message_converts_extended_transmit_frame_with_strange_prefix(self):
        result = CanBusInterface._to_can_message(b'\x07\x07T00144041420180200\r')
        self.assertEqual(result, Message("T", "00144041", 4, [32, 24, 2, 0]))

    def test_to_can_message_converts_extended_transmit_frame_without_data(self):
        result = CanBusInterface._to_can_message(b'T100000010\r')
        self.assertEqual(result, Message("T", "10000001", 0, []))
