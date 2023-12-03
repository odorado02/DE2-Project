import decimal_hour_display
import wifi_connection
import time
from machine import Timer
import ProgramaRelojBinario
import alarma
from machine import Pin

alarm_hour = 0
alarm_minute = 0
alarm = False
button1 = Pin(35, Pin.IN)
led_red = Pin(18, Pin.OUT)
buzzer = Pin(0,Pin.OUT)

"""It is called every second due to the timer. It gets the current hour and displays it in both lcd and led display. Then it checks if the alarm hour and current hour are the same and the buzzer turn on, which is controlled by putting it to low"""

def update_display(t):
    global alarm_hour
    global alarm_minute
    ProgramaRelojBinario.lcd.command(0x01)
    hour, minute = wifi_connection.get_hour()
    decimal_hour_display.write_hour(hour,minute)
    ProgramaRelojBinario.display_hour(hour,minute)
    if alarm_hour == hour and alarm_minute == minute:
        buzzer.off()

"""Connect to the wifi and set the hour"""
wifi_connection.connect_to_wifi(wifi_connection.WIFI_SSID, wifi_connection.WIFI_PASSWORD)
wifi_connection.set_hour()
time.sleep(2)
wifi_connection.disconnect_to_wifi()




timer0 = Timer(0)
timer0.init(period=1000, mode=Timer.PERIODIC, callback=update_display)
buzzer.on()
"""An infinite loop where we are reading the keypad all the time"""
while True:
    k = 0
    sethour = []
    key_pressed = alarma.scan_keypad()
    
if key_pressed == "*":
        alarm = True #Enter into alarm mode

if key_pressed == "D":   #Delete the alarm
        alarm_hour = None
        alarm_minute = None

if button1.value() == 1:  #Turn off the alarm when pushing the button
        buzzer.on()
        alarm_hour = 0
        alarm_minute = 0

while alarm:
        key_pressed = alarma.scan_keypad()
        if key_pressed != "A" and key_pressed != "B" and key_pressed != "D" and key_pressed != "*" and key_pressed != "#" and key_pressed != None and k < 4:

""" We add every number to a list and if we push C we get out of alarm mode and clear the list"""    
            if key_pressed != "C":
                sethour.append(key_pressed)
                print(sethour)
                time.sleep_ms(100)  # Debounce delay
                k = k + 1
            else:
                alarm = False
                sethour.clear()
                k=0
                led_red.on()

"""When we confirm the alarm we check if everything is fine and we save the hour and minutes in two variables. If not we delete it"""

        if key_pressed and k>=4:
            if key_pressed == "A":
                for i in range(4):
                    sethour[i] = int(sethour[i])
                alarm = False
                alarm_hour = sethour[0]*10 + sethour[1]
                alarm_minute = sethour[2]*10 + sethour[3]
                sethour.clear()
                k=0
                if alarm_hour >= 24 or alarm_minute >= 60:
                    alarm_hour = None
                    alarm_minute = None
                    led_red.on()
            if key_pressed == "C":
                alarm = False
                sethour.clear()
                k=0
                led_red.on()
    
    
    time.sleep_ms(500)
    led_red.off()
