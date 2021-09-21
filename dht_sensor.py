from machine import Pin
import dht
from time import sleep_ms

dht = dht.DHT11(Pin(4))
relay = Pin(2, Pin.OUT)

def get_sensor_data():
    dht.measure()
    temperature = dht.temperature()
    humidity = dht.humidity()
    return temperature, humidity

def temperature_humidity_monitor(min_temperature_to_turn_relay_on, min_humidity_to_turn_relay_on):
    min_temperature_to_turn_relay_on
    min_humidity_to_turn_relay_on
    temperature, humidity = get_sensor_data()
    if temperature >= min_temperature_to_turn_relay_on or humidity >= min_humidity_to_turn_relay_on:
        relay.value(1)
    else:
        relay.value(0)
        
def dht_system_loop(min_temperature_to_turn_relay_on,min_humidity_to_turn_relay_on):
    while True:
        temperature_humidity_monitor(min_temperature_to_turn_relay_on,min_humidity_to_turn_relay_on)
        sleep_ms(4000)
        