# Import necessary module(s)
# From `lcd_hd4480.py` file import class `LcdHd4480`
from lcd_hd44780 import LcdHd44780

# Initialize LCD (four-data pins order is [D4, D5, D6, D7])
lcd = LcdHd44780(rs=26, e=25, d=[13, 10, 9, 27])

# Set custom character(s)
# https://www.quinapalus.com/hd44780udg.html

# Cuadrado relleno


def display_hour(hora,minuto):
    new_char = bytearray([0x0,0x1e,0x1e,0x1e,0x1e,0x1e,0x1e,0x1e])
    lcd.custom_char(1, new_char)

    # Cuadrado vacio
    new_char = bytearray([0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0])
    lcd.custom_char(0, new_char)

    # Linea a la derecha
    new_char = bytearray([0x1,0x1,0x1,0x1,0x1,0x1,0x1,0x1])
    lcd.custom_char(2, new_char)

    # Linea a la izquierda
    new_char = bytearray([0x10,0x10,0x10,0x10,0x10,0x10,0x10,0x10])
    lcd.custom_char(3, new_char)

    # Poner limites
    # Primera fila a la izquierda
    lcd.move_to(1, 1)
    lcd.write(chr(2))

    # Primera fila a la derecha
    lcd.move_to(1, 7)
    lcd.write(chr(3))

    #Segunda fila a la izquierda
    lcd.move_to(2, 1)
    lcd.write(chr(2))

    #Segunda fila a la izquierda
    lcd.move_to(2, 8)
    lcd.write(chr(3))
    #Guardarlo a balios binarios
    horabinario= bin(hora)
    minutobinario= bin(minuto)

    #Separarlo a digitos en una lista
    horabinlista = [a for a in str(horabinario)]
    minutobinlista = [b for b in str(minutobinario)]


    #Eliminar primeros dos digitos
    del horabinlista[0]
    del horabinlista[0]
    del minutobinlista[0]
    del minutobinlista[0]

    #Baldintza para que aparezcan ceros al principio si hace falta y nums fila 1
    fila1max = 5
    lcd.move_to(1, 2)

    if fila1max == len(horabinlista):
        for num in horabinlista:
            lcd.write(chr(int(num)))
    else:
        x = fila1max - len(horabinlista)
        for num in range(x):
            lcd.write(chr(0))
        for num in horabinlista:
            lcd.write(chr(int(num)))


    #Baldintza para que aparezcan ceros al principio si hace falta y nums fila 2
    fila2max = 6
    lcd.move_to(2, 2)
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
    
