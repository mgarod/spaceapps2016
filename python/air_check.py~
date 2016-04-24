import time, mraa

# Connect the Grove Air Quality Sensor to analog port A0
# SIG,NC,VCC,GND
air_sensor = 0

def get_quality():
    air = mraa.Aio(1)

    # Get sensor value
    sensor_value = air.read(air_sensor)
    msg = ''
    if sensor_value > 700:
        msg += "High pollution, "
    elif sensor_value > 300:
        msg += "Low pollution, "
    else:
        msg += "Air fresh, "

    msg += "Sensor value: " + str(sensor_value)
