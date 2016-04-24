import gps, temp_check, uv_check, twilio
from Naked.toolshed.shell import execute_js



def main():
    temp = get_temp()
    uv_index = get_uv()
    gps_success = execute_js('main.js')

    phone_number = '+17177468642'
    #phone_number = raw_input("Enter phone number: ")

    if gps_success:
        file = open('lat', 'r')
        lat = file.read()
        file = open('long', 'r')
        lon = file.read()
        msg = "{0}, {1}".format(lat, lon)
        msg += 'Temp: {0}  UV: {1}'.format(temp, uv_index)

        send_Twilio(phone_number, msg)
    else:
        pass # nothing?

main()
