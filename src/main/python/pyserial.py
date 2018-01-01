# import logging
# import serial
# import time
# import datetime
# import asyncio
# from xknx import XKNX
# from influxdb import InfluxDBClient
#
# ser = serial.serial_for_url("/dev/ttyACM0", do_not_open=True)
# ser.baudrate = 115200
# ser.open()
#
# ser.write(b'C\r')
# ser.write(b'S2\r')
# ser.write(b'O\r')
#
# data = {}
#
# mapping = {
#     b"001DC041": {
#         "id": "outlet_fan_air_volume",
#         "name": "Luftmenge Abluftventilator",
#         "unit": "m3",
#     },
#     b"001E0041": {
#         "id": "inlet_fan_air_volume",
#         "name": "Luftmenge Zuluftventilator",
#         "unit": "m3",
#     },
#     b"001D4041": {
#         "id": "outlet_fan_percent",
#         "name": "Leistung Abluftventilator",
#         "unit": "%",
#     },
#     b"001D8041": {
#         "id": "inlet_fan_percent",
#         "name": "Leistung Zuluftventilator",
#         "unit": "%",
#     },
#     b"00458041": {
#         "id": "inlet_temperature",
#         "name": "Temperatur Zuluft",
#         "unit": "^C",
#     },
#     b"00454041": {
#         "id": "outside_temperature",
#         "name": "Temperatur Außenluft",
#         "unit": "^C",
#     },
#     b"00200041": {
#         "id": "power",
#         "name": "Stromverbrauch aktuell",
#         "unit": "W",
#     },
#     b"004C4041": {
#         "id": "inlet_humidity",
#         "name": "Feuchtigkeit Zuluft",
#         "unit": "%",
#     },
#     b"0048C041": {
#         "id": "putlet_humidity",
#         "name": "Feuchtigkeit Abluft",
#         "unit": "%",
#     },
# }
#
# client = InfluxDBClient('localhost', 8086, 'root', 'root', 'ventilation')
#
# try:
#     logging.info("CREATING DATABASE")
#     client.create_database('ventilation')
# except Exception as e:
#     logging.error("create_database: {}".format(e))
#
#
# def get_current_time():
#     return datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
#
#
# def send_metric_datapoint(measurement, location, value, timestamp):
#     json_body = [
#         {
#             "measurement": measurement,
#             "tags": {
#                 "location": location
#             },
#             "time": timestamp,
#             "fields": {
#                 "value": value
#             }
#         }
#     ]
#     try:
#         client.write_points(json_body, database="ventilation")
#     except Exception as e:
#         logging.error("send_metric_datapoint: {}".format(e))
#
#
# try:
#     next = datetime.datetime.now() + datetime.timedelta(minutes=1)
#     print(next)
#     time.sleep(1)
#     while True:
#         out = b''
#         while ser.inWaiting() > 0:
#             char = ser.read(1)
#             if char == b'\r':
#                 break
#             else:
#                 out += char
#
#         if out:
#             raw = out
#             logging.info(raw)
#
#             try:
#                 flag = raw[0:1]
#                 id = raw[1:9]
#
#                 length = int(raw[9:10], 16)
#
#                 index = 10
#                 value = []
#
#                 for item in range(0, length):
#                     value.append(int(raw[index:index + 2], 16))
#                     index += 2
#
#                 if id == b"00454041" or id == b"00458041":
#                     dvalue = (parts[0] - parts[1]) / 10
#                 else:
#                     if len(value) > 1:
#                         parts = value[0:2]
#                         dvalue = float("{}.{}".format(parts[0], parts[1]))
#                     elif len(value) > 0:
#                         dvalue = float(value[0])
#
#                 send_metric_datapoint(id, "hwr", dvalue, get_current_time())
#                 print("{} {} - {} (length: {})".format(flag, id, value, length))
#                 # print(int(value,16))
#
#                 m = mapping.get(id)
#                 if m:
#                     data[m["id"]] = value
#                 else:
#                     data[id] = value
#                 time.sleep(0.1)
#             except Exception as e:
#                 logging.error(e)
#                 logging.exception(e)
#
# # if datetime.datetime.now() > next:
# #      next = datetime.datetime.now() + datetime.timedelta(minutes=1)
# #
# #      print("")
# #      print("")
# #      print(datetime.datetime.now())
# #      for k,v in data.items():
# #        print("{} = {}".format(k,v))
#
# except KeyboardInterrupt:
#     pass
# finally:
#     print("finally closing everything")
#     ser.write(b'C\r')
#     ser.close()
