# Sensirion SGP40 Python 3.x Library

With this library you can read out the VOC index from the Sensirion SGP 40 Sensor.

Installation:
Connect the Sensirion SGP40 sensor to the Raspberry Pi.
- GND
- VDD
- SDA
- SCL

note that I2c is switched on on your Raspberry Pi.

Attention. if you 
`sudo i2cdetect -y 1`
the sensor will not be displayed. this does not mean that the sensor is not working.

Download the files and run `sudo python3 example_sgp40_voc_index.py`
the allgerutmuss now calculates with a default value of 50 %rh and 25°C

To achieve a more realistic accuracy you can connect a SHT30 sensor and run `sudo example_sgp40_and_sht30_voc_index.py`
You can of course also use another temperature and humidity sensor.
To do this, change
`sgp40.set_envparams()` in the loop