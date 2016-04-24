import time
import mraa

# Connect the Grove Air Quality Sensor to analog port A0
# SIG,NC,VCC,GND

get_sensor_value = True
air_sensor_value = 0
air_quality_sensor = mraa.Aio(0)

def main():
    while get_sensor_value:
        try:
            air_sensor_value = air_quality_sensor.readFloat()
            if air_sensor_value > 700:
                print "High pollution!"
            elif air_sensor_value > 300:
                print "Low pollution"
            else:
                print "Air is clean enough."

            print "Sensor value: ", air_sensor_value
            time.sleep(.5)
        except KeyboardInterrupt:
            break
        except IOError:
            print "Can\'t read sensor."

main()
