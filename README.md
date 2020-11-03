# GPS-Grove-in-python
A package for the [GPS Grove] (https://www.seeedstudio.com/Grove-GPS-Module.html), for the BBC micro:bit.


## Code Example
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

## License
MIT

## Supported targets
for BBC micro:bit (The metadata above is needed for package search.
