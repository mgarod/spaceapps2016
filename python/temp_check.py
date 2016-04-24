import time, mraa

# Connected Grove temp sensor to analog port A2

def main():
    while True:
        try:
            temp_sensor = mraa.Aio(2)
            temp = temp_sensor.readFloat()
            print "Temperature: ", temp

        except KeyboardInterrupt:
            break
        except IOError:
            print "Could not read temperature."

main()
