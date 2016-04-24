import time, mraa

def get_dust():
    try:
    	x = mraa.Gpio(3)
        x.dir(mraa.DIR_IN)
        dust_val = x.read()
        return dust_val
