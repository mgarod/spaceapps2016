import mraa

# Connected Grove temp sensor to analog port A3

def get_uv():
    try:
        uv_sensor = mraa.Aio(3)
        Vsig = uv_sensor.readFloat()
        intensity = 307 * Vsig # 307 taken from documentation.
        msg = ''
        uv_idx = intensity // 200
#        print uv_idx
        return uv_idx
    except IOError:
        print 'IO Error!'
        return
get_uv()
