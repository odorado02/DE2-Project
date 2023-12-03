import network
import time
from machine import RTC
import ntptime

WIFI_SSID = "UREL-SC661-V-2.4G"
WIFI_PASSWORD = "TomFryza"
UTC_OFFSET = 1

wifi = network.WLAN(network.STA_IF)
rtc = RTC()


def connect_to_wifi(ssid, password):
    
    if not wifi.isconnected():
        wifi.active(True)
        
        try:
            wifi.connect(ssid, password)
            while not wifi.isconnected():
                time.sleep_ms(150)
            print("Connected")
        except:
            print("Problems connecting to the wifi")

def disconnect_to_wifi():
    
    if wifi.active():
        wifi.active(False)
    
    if not wifi.isconnected():
        print("Disconnected")
    
def set_hour():
    ntptime.settime()
    sec = ntptime.time()
    sec = int(sec + UTC_OFFSET * 60 * 60)
    (year, month, day, hrs, mins, secs, wday, yday) = time.localtime(sec)
    rtc.datetime((year, month, day, wday, hrs, mins, secs, 0))

def get_hour():
    (year, month, day, wday, hrs, mins, secs, subsecs) = rtc.datetime()
    return hrs, mins
    

"""connect_to_wifi(WIFI_SSID, WIFI_PASSWORD)
set_hour()
time.sleep(2)
disconnect_to_wifi()
    
while True:
    # Read values from internal RTC
    hour, minutes = get_hour()
    print(f"{hrs}:{mins}")

    # Delay 30 seconds
    time.sleep(2)"""
    

