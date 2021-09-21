import wlan_lib
import dht_sensor

wlan_lib.connect_to_wifi('','')
dht_sensor.dht_system_loop(30,71)
