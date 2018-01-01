from multiprocessing import Process, Manager
from zcan.can import CanBusReader
import time


def main():
    manager = Manager()
    measurements = manager.dict()
    unknown_messages = manager.dict()

    def input(m, u):
        CanBusReader().read_messages(m, u)

    def measurements_outputs(m):
        while True:
            print(m)
            time.sleep(2)

    def unknowns_output(u):
        while True:
            for item in u.items():
                print(item)
            time.sleep(60)

    p1 = Process(target=input, args=(measurements, unknown_messages,))
    p2 = Process(target=measurements_outputs, args=(measurements,))
    p3 = Process(target=unknowns_output, args=(unknown_messages,))

    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
