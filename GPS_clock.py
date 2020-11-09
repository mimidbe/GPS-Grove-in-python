from microbit import *
import GPS_GROVE

monGPS = GPS()

while True:
  if monGPS.ready():
    Clock = monGPS.getInformations(info=1)
    if Clock != None:
      display.scroll(str(''.join([str(x) for x in [Clock[0], 'h', Clock[1], 'm', Clock[2], 's']])))
