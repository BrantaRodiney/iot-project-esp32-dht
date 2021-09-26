from time import time, sleep

import wlan_lib
import dht_sensor
import thingspeak_lib

print('Temperature and Humidity Monitor')

ssid = input("Enter your router SSID: ")
pwd = input("Enter your router password: ")

temperature_msg = "Enter the max temperature before relay turns on: "
temperature = int(input(temperature_msg))

humidity_msg = "Enter the max humidity before relay turns on: "
humidity = int(input(humidity_msg))

time_interval_thingspeak_msg = \
    "Enter the time(sec) interval before sending new measures to ThingSpeak: "
time_interval_thingspeak = int(input(time_interval_thingspeak_msg))

time_interval_local_msg = \
    "Enter the time(sec) interval before relay activation: "
time_interval_local = int(input(time_interval_local_msg))

wlan_lib.connect_to_wifi(ssid,pwd)

start_time = int(time()) 
while (True):
    elapsed_time = int(time()) - start_time
    if elapsed_time % time_interval_thingspeak == 0:
        thingspeak_lib.send_data()
    if elapsed_time % time_interval_local == 0:
        dht_sensor.temperature_humidity_monitor(temperature,humidity)
    sleep(1)
