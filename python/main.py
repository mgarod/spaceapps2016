from Naked.toolshed.shell import execute_js
from temp_check import get_temp
from uv_check import get_uv
from twiliosms import send_Twilio
from air_check import get_quality
import socket
import fcntl
import struct

import pyupm_i2clcd as lcd
myLcd = lcd.Jhd1313m1(0, 0x3E, 0x62)

# Clear
myLcd.clear()

# Green
myLcd.setColor(255, 255, 255)

# Zero the cursor
myLcd.setCursor(0,0)

def main():
    phone_number = '+17177468642' 
    #phone_number = raw_input("Enter phone number: ")
    #gps_success = execute_js('main.js')

    #while True:
    uv_index = get_uv()
    temp = get_temp()
    airq = get_quality()
    print airq

    # if gps_success:
    #     print "GPS Success"
    file = open('lat', 'r')
    lat = file.read()
    file = open('long', 'r')
    lon = file.read()
    msg = "({0}, {1})".format(lat, lon)
    lcd1 = "({0}, {1})".format(lat, lon)
    msg += 'Temp: {0}  UV: {1} Air Quality: {2}'.format(temp, uv_index, airq)
    lcd2 = 'UV: {0} Temp {1}'.format(uv_index, temp)
    lcd3 = 'Air Quality: {0}'.format(airq)

    send_Twilio(phone_number, msg)
    myLcd.setCursor(0,0)
    myLcd.write(lcd2)
    myLcd.setCursor(1,0)
    myLcd.write(lcd3)

    send_Twilio(phone_number, msg)
    #else:
    #    break # nothing?

main()
