import network
import time
from machine import RTC
import ntptime

WIFI_SSID = "UREL-SC661-V-2.4G"
WIFI_PASSWORD = "TomFryza"
UTC_OFFSET = 1  #The hour difference with the UTC hour 

wifi = network.WLAN(network.STA_IF) #Set our device as station
rtc = RTC()

"""This function checks if there is already connected to a wifi and if not it activates it and then connect to the defined wifi"""

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

"""We set the ESP32 to the current time. After we get the time in seconds we add the offset in seconds and then we update the rtc"""    
def set_hour():
    ntptime.settime()
    sec = ntptime.time()
    sec = int(sec + UTC_OFFSET * 60 * 60)
    (year, month, day, hrs, mins, secs, wday, yday) = time.localtime(sec)
    rtc.datetime((year, month, day, wday, hrs, mins, secs, 0))

"""It asks for the current time and returns the hours and minutes"""
def get_hour():
    (year, month, day, wday, hrs, mins, secs, subsecs) = rtc.datetime()
    return hrs, mins
    
    
