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
