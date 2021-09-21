import network
from network import WLAN
from time import sleep_ms

network.WLAN(network.STA_IF).active(False)

def scan_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    state = wlan.active()
    for ssid in wlan.scan():
        print('Network Info:', ssid)
    wlan.active(state)
    
def network_status():
    wlan = network.WLAN(network.STA_IF)
    status = wlan.status()
    return int_status_to_name(status)
    
def network_info():
    wlan = network.WLAN(network.STA_IF)
    return wlan.ifconfig()
    
def connect_to_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
       print('Connecting to network', ssid)
       wlan.connect(ssid, password)
       for attempt in range(40):
           status = wlan.status()
           if status == network.STAT_GOT_IP:
               return int_status_to_name(status), True
           if status != network.STAT_CONNECTING:
               return int_status_to_name(status), False
           sleep_ms(100)             
    return 'Timeout', False
      
def int_status_to_name(status_as_int):
    switcher = {
        1000: 'STAT_IDLE',
        1001: 'STAT_CONNECTING',
         202: 'STAT_WRONG_PASSWORD',
         201: 'STAT_NO_AP_FOUND',
        1010: 'STAT_GOT_IP'
    }
    return switcher.get(status_as_int, 'Unknown Status: (' + str(status_as_int) + ')')
