import mraa

# Connected Grove temp sensor to analog port A2

def get_temp():
    try:
        temp_sensor = mraa.Aio(2)
        t = temp_sensor.readFloat()
        resistance = (1023 - t) * 10000.0 / t
        temp = 1 / (math.log(resistance / 10000.0) / B + 1 / 298.15) - 273.15
        return temp
    except IOError:
        return
