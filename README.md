# DE2-Project

### Team members

- **David Corrionero**: Responsible for WiFi connection and syncronization with network time servers
- **Aitana del Carmen**: Responsible for converting current time from decimal to binary
- **Oier Dorado**: Responsible for alarms and its additional features (such as sounds, confirmation via led)

## Theoretical description and explanation

*Task: Digital clock Max 2 groups. Design and implement a digital clock using the MicroPython programming language on the ESP32 microcontroller. The clock will not only display the current time in both decimal and binary formats but will also include additional features such as alarms and synchronization with network time servers*

The digital clock is firstly connected to the network in order to get the current time as fast as possible. The process of taking the time is repeated every second using a timer. Next, the display shows the current time in binary and in normal format and they are updated every second also.

Apart from that, alarms can be set as soon as the digital clock gets the current time. On the one hand, there is a keypad with which you can write the alarm time and the value is saved automatically in the code; Furthermore, whenever the hour written is not coherent, a red light is turned on with a view to warn you about the error and the value is eliminated. On the other hand, there is a buzzer that starts working when the alarm set matches the current time and the blue button needs to be pressed to stop such alarm.

## Hardware description and demo application

Insert descriptive text and schematic(s) of your implementation.

![IMG_2538](https://github.com/odorado02/DE2-Project/assets/147071596/64031a4d-3fd3-4cf4-825a-d9b72c0b244e)

The hardware is composed by 7 components:

- ESP32 microcontroller: The component which runs all the program and coordinates all the other components. Also is the ono which connects to the network in order to get the hour.

<img src="https://github.com/odorado02/DE2-Project/assets/147071596/2956e84d-94d4-4496-9a73-d8aec0ac8f43" width="450" height="350">

- Keypad: Used to set the alarm configuration.

<img src="https://github.com/odorado02/DE2-Project/assets/147071596/71590375-a94c-4f7e-bc0c-013cf2f32011" width="450" height="350">

- LCD screen module: Display used to show the time in binary.

<img src="https://github.com/odorado02/DE2-Project/assets/147071596/3980f3cf-db62-42bc-9afa-33a6c91bd2a3" width="450" height="350">

- 7 segment LED display module: Display used to show the time in normal format.

<img src="https://github.com/odorado02/DE2-Project/assets/147071596/3863e896-ed7a-43d6-9130-6c2febf03244" width="450" height="350">

- Red LED: This led will turn on when the alarm set is incorrect.

<img src="https://github.com/odorado02/DE2-Project/assets/147071596/f71aac22-09a5-40e8-a4d9-aef7ff05a5c9" width="450" height="350">

- Multi-function shield: Although this module has a lot of different functions we only used the buzzer from it. When time reaches the alarm hour the buzzer will turn on.

<img src="https://github.com/odorado02/DE2-Project/assets/147071596/1b4324a8-233a-4bef-a492-47ee81762e16" width="450" height="350">

- Resistance:

<img src="https://github.com/odorado02/DE2-Project/assets/147071596/aa801cf2-aa3d-4b31-8ce6-42dd8f21281d" width="450" height="350">

- Button: Used to stop the alarm.

<img src="https://github.com/odorado02/DE2-Project/assets/147071596/033e2776-20c4-4a4b-9f6e-74076d80a5df" width="450" height="350">

## Software description

List of codes:

`main.py`: This is the main program to run. This program configures the timers, the global variables, updates the displays and sets the alarm.
```Python
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
```

`BinaryHourDisplay.py`: This program is the one in charge of displaying the binary time in the LCD display.
```Python
# Import necessary module(s)
# From `lcd_hd4480.py` file import class `LcdHd4480`
from lcd_hd44780 import LcdHd44780

# Initialize LCD (four-data pins order is [D4, D5, D6, D7])
lcd = LcdHd44780(rs=26, e=25, d=[13, 10, 9, 27])

# Set custom character(s)
# https://www.quinapalus.com/hd44780udg.html


def display_hour(hora,minuto):
    # Filled up square
    new_char = bytearray([0x0,0x1e,0x1e,0x1e,0x1e,0x1e,0x1e,0x1e])
    lcd.custom_char(1, new_char)

    # Empty square
    new_char = bytearray([0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0])
    lcd.custom_char(0, new_char)

    # Limit line on the right
    new_char = bytearray([0x1,0x1,0x1,0x1,0x1,0x1,0x1,0x1])
    lcd.custom_char(2, new_char)

    # Limit line on the left
    new_char = bytearray([0x10,0x10,0x10,0x10,0x10,0x10,0x10,0x10])
    lcd.custom_char(3, new_char)

    # Placing limits

    # First row on the left
    lcd.move_to(1, 1)
    lcd.write(chr(2))

    # First row on the right
    lcd.move_to(1, 7)
    lcd.write(chr(3))

    # Second row on the left
    lcd.move_to(2, 1)
    lcd.write(chr(2))

    # Second row on the right
    lcd.move_to(2, 8)
    lcd.write(chr(3))

    # Changing the current time from decimal to binary
    horabinario= bin(hora)
    minutobinario= bin(minuto)

    # Separate the curren time in binary to a list
    horabinlista = [a for a in str(horabinario)]
    minutobinlista = [b for b in str(minutobinario)]


    # Delete first two digits 
    del horabinlista[0]
    del horabinlista[0]
    del minutobinlista[0]
    del minutobinlista[0]

    # Placing zeros if neccesary at the beginning and placing the respective symbols in row 1
    fila1max = 5
    lcd.move_to(1, 2)     # Moving cursor to that position to avoid overwriting

    if fila1max == len(horabinlista):
        for num in horabinlista:
            lcd.write(chr(int(num)))
    else: 
        x = fila1max - len(horabinlista)
        for num in range(x):
            lcd.write(chr(0))
        for num in horabinlista:
            lcd.write(chr(int(num)))


    # Placing zeros if neccesary at the beginning and placing the respective symbols in row 2
    fila2max = 6
    lcd.move_to(2, 2)     # Moving cursor to that position to avoid overwriting

    if fila2max == len(minutobinlista):
        for num in minutobinlista:
            lcd.write(chr(int(num)))
    else:
        y = fila2max - len(minutobinlista)
        for num in range(y):
            lcd.write(chr(0))
        for num in minutobinlista:
            lcd.write(chr(int(num)))

        # Optional cleanup code
        #lcd.command(0x01)  # Clear display
```

`wifiConnection.py`: This program connects the ESP32 to the wifi network and there are also functions to ask for the current time. `tm1367`is
```Python
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

"""This function disconnects the microcontroller from the wifi"""
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

```

`DecimalHourDisplay.py`: This code is the one in charge of displaying the decimal hour in the seven segment module display. We downloaded a library `tm1637` for the display.
```Python
import tm1637
from machine import Pin

tm = tm1637.TM1637(clk=Pin(5), dio=Pin(2)) #Configuration of the led display
tm.brightness(val=7)

def write_hour(hour,minutes):
    tm.numbers(hour, minutes)
```

`ScanMatrixKeypad.py`: This function scans the key pressed in the matrix keypad and returns its value.
```Python
from machine import Pin
import time

# Define the GPIO pins for rows (outputs) and columns (inputs with pull-ups)
row_pins = [Pin(pin, Pin.OUT) for pin in (19, 21, 22, 14)]
col_pins = [Pin(pin, Pin.IN, Pin.PULL_UP) for pin in (12, 4, 16, 17)]

# Define the keypad matrix layout
keypad = [
    ["1", "2", "3", "A"],
    ["4", "5", "6", "B"],
    ["7", "8", "9", "C"],
    ["*", "0", "#", "D"],
]


"""It scans the keypad and returns the key"""
def scan_keypad():
    key = None

    for row_num in range(len(row_pins)):
        # Set the current row LOW and the rest HIGH
        for r in range(len(row_pins)):
            row_pins[r].value(0 if r == row_num else 1)

        # Wait for signal to settle
        time.sleep_us(10)

        for col_num in range(len(col_pins)):
            # Read the column input
            if col_pins[col_num].value() == 0:
                key = keypad[row_num][col_num]
                while not col_pins[col_num].value():
                    pass  # Wait for key release

    return key
```

## Instructions

**Binary Clock**

In binary, for the values that equal 1 in the hour on binary, the display shows black blocks, and similarly, for the values that equal zero, the display leaves the blocks in blank.

**Setting Alarm**

1. Press "*" to start.
1. Write your alarm by pressing 4 numbers (correct form: HHmm), otherwise there will be an error and the red led will turn on.
1. Press "A" (Accept) if the alarm time is the one you want. Otherwise press "C" (Cancel) and repeat step 2.
1. If you want to change the alarm set, repeat steps 1 2 3 again.
1. The alarm buzzer will sound when the alarm time is the same as the current time.
1. To stop the alarm buzzer the blue button needs to be pressed.
1. To delete the alarm you can press "*" to set a new alarm or you can press "D" to delete the current alarm and not to configure another alarm.


