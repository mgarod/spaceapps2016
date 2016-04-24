import time
import mraa

# Connect the Grove Air Quality Sensor to analog port A1
# SIG,NC,VCC,GND

get_sensor_value = True
air_sensor_value = 0
air_quality_sensor = mraa.Aio(1)

class AirQuality:
    self.i = 0
    self.init_volt = 0
    self.volt_std = 0
    self.first_volt = 0
    self.last_volt = 0
    self.temp = 0
    self.counter = 0
    self.timer_idx = 0
    self.error = False

    def get_volt(self):
        return self.volt_std

    def init(self):
        aq = mraa.Aio(1)
        self.i = 0
        time.sleep(300)
        self.init_volt = mraa.readFloat()
        while self.init_volt != 0:
            if self.init_volt < 798 and self.init_volt > 10:
                self.first_volt = mraa.readFloat()
                self.last_volt = self.first_volt
                self.volt_std = self.last_volt
                break
            elif self.init_volt > 798 or self.init_volt <= 10:
                self.i += 1
                time.sleep(600)
                self.init_volt = mraa.readFloat()
                if self.i == 5:
                    self.i = 0
                    self.error = True
                    print "Sensor error.\n"
            else:
                break

    def avg_volt(self):
        if self.i == 150:
            self.volt_std = self.temp / 150
            self.temp = 0
            self.i = 0
            print "Voltage standard: " + str(self.volt_std)
        else:
            self.temp += self.first_volt
            self.i += 1

    def slope(self):
        msg = ''
        while self.timer_idx != 0:
            if self.first_volt - self.last_volt > 400 or self.first_volt > 700:
                msg = 'High pollution! Action required!'
                self.timer_idx = 0
                self.avg_volt()
            return
            elif self.first_volt - self.last_volt > 400 and self.first_volt < 700 or self.first_volt - self.volt_std > 150:
                msg = "Sensor value: " + str(self.first_volt) + '\n'
                msg += "High pollution. No action required.\n"
                self.timer_idx = 0
                self.avg_volt()
                return
            elif self.first_volt - self.last_volt > 200 and self.first_volt < 700 or self.first_volt - self.volt_std > 50:
                msg = 'Sensor value: ' + str(self.first_volt)
                msg += '\nLow pollution.\n'
                self.timer_idx = 0
                self.avg_volt
                return
            else:
                self.avg_volt()
                msg = 'Sensor value: ' + str(self.first_volt)
                msg += '\n Clean.\n'
                self.timer_idx = 0
                return
        return
