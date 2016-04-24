import time
import mraa

# Connect the Grove Air Quality Sensor to analog port A0
# SIG,NC,VCC,GND

get_sensor_value = True
air_sensor_value = 0
air_quality_sensor = mraa.Aio(1)

def get_air_quality():
    '''Returns a tuple, a float value and a string.'''
    try:
        air_sensor_value = air_quality_sensor.readFloat()
        pollution = ''
        if air_sensor_value > 700:
            pollution = "High pollution!""
        elif air_sensor_value > 300:
            pollution = "Low pollution."
        else:
            pollution = "Air is clean enough."
        return air_sensor_value, pollution
    except IOError:
        print "Can\'t read sensor."

main()
