from multiprocessing import Process, Manager
from zcan.can import CanBusReader
import time

from zcan.influxdb_writer import InfluxDbWriter
from zcan.util import get_logger


def main():
    logger = get_logger()
    manager = Manager()
    measurements = manager.dict()
    unknown_messages = manager.dict()

    def input(m, u):
        CanBusReader().read_messages(m, u)

    def measurements_outputs(m):
        writer = InfluxDbWriter()
        while True:
            logger.info("Sending values to influxdb")
            for item in m.values():
                logger.debug("Sending to influxdb: {}".format(item))
                writer.send_metric_datapoint(item)

            time.sleep(10)

    def unknowns_output(u):
        while True:
            logger.info("Unknown messages so far")
            for item in u.values():
                logger.warn(item)
            time.sleep(3600)

    p1 = Process(target=input, args=(measurements, unknown_messages,))
    p2 = Process(target=measurements_outputs, args=(measurements,))
    p3 = Process(target=unknowns_output, args=(unknown_messages,))

    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
