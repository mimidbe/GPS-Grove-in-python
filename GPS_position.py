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
