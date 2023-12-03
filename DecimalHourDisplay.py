import tm1637
from machine import Pin

tm = tm1637.TM1637(clk=Pin(5), dio=Pin(2))
tm.brightness(val=7)

def write_hour(hour,minutes):
    tm.numbers(hour, minutes)
