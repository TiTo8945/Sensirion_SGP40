import time
from Sensirion_SGP40 import Sensirion_SGP40
from Sensirion_SHT30 import Sensirion_SHT30

#set IICbus elativeHumidity(0-100%RH)  temperature(-10~50 centigrade)
sgp40=Sensirion_SGP40(bus = 1, relative_humidity = 50, temperature_c = 25)

sht30=Sensirion_SHT30()

#set Warm-up time
print('Please wait 10 seconds...')
sgp40.begin(10)

while True:
    sht30.sht30_read()
    sgp40.set_envparams(sht30.humidity, sht30.temperature)
    print('Voc index:  %d Temperature: %8.2f°C humidity: %8.2frh' % (sgp40.get_voc_index(), sht30.temperature, sht30.humidity))
    time.sleep(1)