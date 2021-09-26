import urequests
from time import sleep_ms

import dht_sensor

THINGSPEAK_APT_WRITE_KEY = ''
THINGSPEAK_API_READ_KEY = ''
HTTP_HEADER= {'Content-Type': 'application/json'}

def receive_sensor_data_and_post_it():
    temperature, humidity = dht_sensor.get_sensor_data()
    send_data(temperature,humidity)
    print(temperature,humidity)
    
def send_data(temperature, humidity):
    request = urequests.post(
        'http://api.thingspeak.com/update?api_key=' +
        THINGSPEAK_APT_WRITE_KEY,
        json = {'field1':temperature,'field2':humidity},
        headers = HTTP_HEADER
    )
    request.close()
