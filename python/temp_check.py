import mraa
import math

# Connected Grove temp sensor to analog port A2

#B=3975

def get_temp():
    # try:
    #     temp_sensor = mraa.Aio(2)
    #     t = temp_sensor.read()
    #     #resistance = (1023 - t) * 10000.0 / t
    #     #temp = 1 / (math.log(resistance / 10000.0) / B + 1 / 298.15) - 273.15
    #     temp=t*.5;
    #     temp/=1024.0;
    #     return temp
    # except IOError:
    #     return
    #B = 3975
    ain = mraa.Aio(2)
    a = ain.read()
    resistance = (1023-a)*10000.0/a
    temp = 1/(math.log(resistance/10000.0)3975+1/298.15)-273.15
    return temp
# =======
#     try:
#         temp_sensor = mraa.Aio(2)
#         t = temp_sensor.readFloat()
#         #resistance = (1023 - t) * 10000.0 / t
#         #temp = 1 / (math.log(resistance / 10000.0) / B + 1 / 298.15) - 273.15
#         temp=t*.5;
#         temp/=.010240;
#         return temp
#     except IOError:
#         return
# >>>>>>> refs/remotes/origin/master
