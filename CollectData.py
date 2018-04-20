import datetime
import json

import requests
import serial

from gasPrototypeNode.SensorsRawData import SensorsRawData

ser = serial.Serial('/dev/cu.usbmodem14141',9600)

register = {}

LOCATION = 'Kitchen'


def to_timestamp():
    return datetime.datetime.now().timestamp()


def save_on_mongodb(parameter):
    headers = {'Content-type': 'application/json'}
    r = requests.post("http://186.4.148.194:8045/data_collect/ppmData.php",
                      headers=headers, data=json.dumps(parameter))


while True:
    incoming = ser.readline().strip()
    parse_cad = incoming.decode().split("-")
    sensor_data = SensorsRawData('01', parse_cad[1], parse_cad[2], parse_cad[0], to_timestamp(), LOCATION)
    register["nodo"] = sensor_data.get_node()
    register["mq2"] = int(sensor_data.get_mq2())
    register["mq7"] = int(sensor_data.get_mq7())
    register["mq135"] = int(sensor_data.get_mq135())
    register["fecha"] = sensor_data.get_date()
    register["ubicacion"] = sensor_data.get_location()
    print(json.dumps(register))
    save_on_mongodb(register)

