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
