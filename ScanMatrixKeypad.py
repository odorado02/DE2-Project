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

"""alarm = False
alarm_hour = None
alarm_minute= None"""


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

                
    """if alarm_hour != None and alarm_minute != None:
        return alarm_hour,alarm_minute"""

# Forever loop until interrupted by Ctrl+C. When Ctrl+C
# is pressed, the code jumps to the KeyboardInterrupt exception
"""while True:
    key_pressed = scan_keypad()
    if key_pressed == "*":
        alarm = True
    while alarm:
        key_pressed = scan_keypad()
        if key_pressed != "A" and key_pressed != "B" and key_pressed != "D" and key_pressed != "*" and key_pressed != "#" and key_pressed != None and k < 4:
            if key_pressed != "C":
                sethour.append(key_pressed)
                print(sethour)
                time.sleep_ms(100)  # Debounce delay
                k = k + 1
            else:
                alarm = False
                sethour.clear()
                k=0
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
            if key_pressed == "C":
                alarm = False
                sethour.clear()
                k=0"""
