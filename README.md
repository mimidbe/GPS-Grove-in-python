# GPS-Grove-in-python
A package for the [GPS Grove](https://www.seeedstudio.com/Grove-GPS-Module.html), for the BBC micro:bit.

![logo](https://github.com/mimidbe/GPS-Grove-in-python/blob/main/images/GPS_Grove.png)

## Code Examples 
sample code to display the GPS time on the BBC micro:bit display.

```Python
from microbit import *
import GPS_GROVE

monGPS = GPS_GROVE

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

monGPS = GPS_GROVE

while True:
  if monGPS.ready():
    lat = monGPS.getInformations(info=2)
    lon = monGPS.etInformations(info=4)
    if lat != None and lon != None:
      display.scroll(str(str(lat) + str(" 'N")))
      display.scroll(str(str(lon) + str(" 'E")))

```

## License
MIT

## Supported targets
for BBC micro:bit (The metadata above is needed for package search.
