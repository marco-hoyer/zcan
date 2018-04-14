from multiprocessing import Process, Manager
from zcan.can import CanBus
import time

from zcan.influxdb_writer import InfluxDbWriter
from zcan.util import get_logger

logger = get_logger()


def write(payload):
    CanBus().write(payload)


def write_ventilation_level(iterator):
    messages = [
        bytes("T1F0{}505180084150101000000".format(iterator), encoding="ASCII"),
        bytes("T1F0{}505180100201C00000300".format(iterator), encoding="ASCII"),
        bytes("T1F0{}14410".format(int(iterator) - 1), encoding="ASCII")
    ]
    CanBus().write_messages(messages)


def get_error_state():
    CanBus().get_error_state()


def listen(all: bool):
    CanBus().print_messages(all)


def main():
    manager = Manager()
    measurements = manager.dict()
    unknown_messages = manager.dict()

    p1 = Process(target=read_can_bus, args=(measurements, unknown_messages,))
    p2 = Process(target=write_to_influxdb, args=(measurements,))
    # p3 = Process(target=log_unknown_messages, args=(unknown_messages,))

    p1.start()
    p2.start()
    # p3.start()
    p1.join()
    p2.join()
    # p3.join()


def read_can_bus(m, u):
    while True:
        try:
            CanBus().read_messages(m, u)
        except Exception as e:
            logger.exception(e)


def write_to_influxdb(m):
    writer = InfluxDbWriter()
    while True:
        try:
            logger.info("Sending values to influxdb")
            for item in m.values():
                logger.debug("Sending to influxdb: {}".format(item))
                writer.send_metric_datapoint(item)
        except Exception as e:
            logger.exception(e)

        time.sleep(10)


def log_unknown_messages(u):
    while True:
        logger.info("Unknown messages so far")
        for item in u.values():
            logger.warn(item)
        time.sleep(3600)
