import mraa

# Connected Grove temp sensor to analog port A2

def get_uv():
    try:
        uv_sensor = mraa.Aio(3)
        Vsig = uv_sensor.readFloat()
        intensity = 307 * Vsig # 307 taken from documentation.
        msg = ''
        uv_idx = intensity // 200
        return uv_idx
    except IOError:
        return
