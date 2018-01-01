from influxdb import InfluxDBClient

from zcan.can import Measurement
from zcan.util import get_logger, get_current_time


class InfluxDbWriter(object):
    def __init__(self, host="localhost", port=8086, user="root", password="root", db="zcan"):
        self.logger = get_logger("InfluxDbWriter")
        self.db = db

        self.client = InfluxDBClient(host, port, user, password, db)
        self.client.create_database(db)

    def send_metric_datapoint(self, measurement: Measurement, timestamp=get_current_time()):
        json_body = [
            {
                "measurement": measurement.name,
                "tags": {
                    "location": measurement.id,
                    "unit": measurement.unit
                },
                "time": timestamp,
                "fields": {
                    "value": measurement.value
                }
            }
        ]
        try:
            self.client.write_points(json_body, database=self.db)
        except Exception as e:
            self.logger.error(e)
