# GPS-Grove-in-python
A package for the [GPS Grove](https://www.seeedstudio.com/Grove-GPS-Module.html), for the BBC micro:bit.

![logo](https://github.com/mimidbe/GPS-Grove-in-python/blob/main/images/GPS_Grove.png)

The data received by the module are frames from the NMEA 083 standard. There are several types of frames including GPGGA and GPRMC. Here is an example of a valid GPGGA frame:

$ GPGGA,163221.000,4854.8644,N,00219.4940,E,2,9,0.94,52.1,M,47.3

It provides the following information:

- info n°1: Clock: 16h 32m 21s

- info n°2 & 3:Latitude: 4854.8644 N

- info n°4 & 5:Longitude: 219.4940 E

- info n°7:Number of satellites used: 9

- info n°8:Altitude: 52.1 m



## Code Examples 
sample code to display the GPS time on the BBC micro:bit display.

```Python
from microbit import *
import GPS_GROVE

monGPS = GPS()

while True:
  if monGPS.ready():
    Clock = monGPS.getInformations(info=1)
    if Clock != None:
      display.scroll(str(''.join([str(x) for x in [Clock[0], 'h', Clock[1], 'm', Clock[2], 's']])))

```


sample code to display the GPS position on the BBC micro:bit display.

```Python
from microbit import *
import GPS_GROVE

monGPS = GPS()

while True:
  if monGPS.ready():
    lat = monGPS.getInformations(info=2)
    lon = monGPS.getInformations(info=4)
    if lat != None and lon != None:
      display.scroll(str(str(lat) + str(" 'N")))
      display.scroll(str(str(lon) + str(" 'E")))

```

## License
MIT

## Supported targets
for BBC micro:bit
