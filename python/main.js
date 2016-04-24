var m = require('mraa'); //require mraa
var fs = require('fs'); // require filesystem

u = new m.Uart(0);
console.log(u.getDevicePath());

var SerialPort = require("serialport").SerialPort
var serialPort = new SerialPort(u.getDevicePath(), {
  baudrate: 9600
});

// check for lowest number in dir "new" -> to determin file to write data to
var new_file = '';
var files_in_new = [];
fs.readdirSync("/home/root/gps_data/new").forEach(function(file) {
    console.log(file);
    files_in_new.push(file);
});
console.log('files_in_new', files_in_new);

for (i = 0; i < 100; i++) {
    new_file = '' + i;
    if (files_in_new.indexOf(new_file) <= -1) {
        break;
    }
}



// receive GPS (approx every second)

//write all received data into new_file
serialPort.on("open", function () {
  console.log('open');
  serialPort.on('data', function(data) {
      var data_string = '' + data
      if (data_string.substring(0,6) == '$GPGGA') {
          gpgga_string = data_string.split('\n')[0];
          gpgga_string = gpgga_string.replace('\n', '');
          gps_data = gpgga_string.split(',');
          console.log('data received: ' + gps_data);
          var time_string = gps_data[1];
          var gps_time = new Date();
          var gps_time_hours = parseInt(gps_data[1].substring(0,2));
          var gps_time_minutes = parseInt(gps_data[1].substring(2,4));
          var gps_time_seconds = parseInt(gps_data[1].substring(4,6));
          gps_time.setHours(gps_time_hours);
          gps_time.setMinutes(gps_time_minutes);
          gps_time.setSeconds(gps_time_seconds);
          
          gps_lat = gps_data[2];
          gps_lat_ns = gps_data[3];
          gps_lon = gps_data[5];
          gps_lon_ew = gps_data[6];
          console.log('gps_time', gps_time);
          console.log(gps_lat, gps_lat_ns);
          

          
          fs.writeFile("/home/root/gps_data/new/" + "gps", gps_time + ';' + gps_data + '\n', function(err) {
              if(err) {
                return console.log(err);
            }
              console.log("line was aappended to file", gps_time + ';' + gps_data + ';');
          }); 

      }
  });
});


// round off output to match C example, which has 6 decimal places
function roundNum(num, decimalPlaces)
{
	var extraNum = (1 / (Math.pow(10, decimalPlaces) * 1000));
	return (Math.round((num + extraNum) 
		* (Math.pow(10, decimalPlaces))) / Math.pow(10, decimalPlaces));
}




/*
// B L U E T O O T H
var bleno = require('bleno');
var uuid = 'e2c56db5dffb48d2b060d0f5a71096e0';
var major = 0; // 0x0000 - 0xffff
var minor = 0; // 0x0000 - 0xffff
var measuredPower = -59; // -128 - 127

bleno.startAdvertisingIBeacon(uuid, major, minor, measuredPower[, callback(error)]);'*/
