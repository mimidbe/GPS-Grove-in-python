from microbit import *

# GPS on UART
class GPS:
	def __init__(self,baudrate=9600,tx=pin14, rx=pin0):
	  uart.init(baudrate, bits=8, parity=None, stop=1, tx, rx)
	
	def ready():
	  return uart.any()

	def getInformations(info = 0):	  
	  data = str(uart.read()).split(',')
	  if len(data) > 10:
		if 'GPGGA' in data[0] or 'GAGGA' in data[0] or 'BDGGA' in data[0] or 'GBGGA' in data[0] or 'GLGGA' in data[0] or 'GNGGA' in data[0]:
		  if info == 0 or info == 7:
			if data[info] != None and data[info] != '':
			  return data[info]
		  if info == 1 :
			if data[1] != None:
			  return self.__getTime(data[1])
		  if info == 2 or info == 4:
			if data[info] != None:
			  return self.__getPosition(data[info])
		  if info == 9 :
			if float(data[9]) != None:
			  return float(data[9])
	  return None

	def __getTime(date):
	  if date and float(date):
		h = int(float(date) / 10000)
		m = int((float(date) - h*10000) / 100)
		s = int(float(date) - h*10000 - m*100)
		return (h, m, s)

	def __getPosition(pos):
	  if pos and float(pos):
		base = int(float(pos)/100)
		mn = float(pos) - base*100
		return "%03.5f"%(base + mn/60)
