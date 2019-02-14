import urllib2
import binascii
import sys

import Adafruit_PN532 as PN532

ip = 'http://10.10.97.22:5000'

# Setup how the PN532 is connected to the Raspbery Pi/BeagleBone Black.
# It is recommended to use a software SPI connection with 4 digital GPIO pins.

# Configuration for a Raspberry Pi:
CS   = 17
MOSI = 23
MISO = 24
SCLK = 25

# Main loop to detect cards and read a block.
print('Waiting for MiFare card...')

var = 0

def reader():
#Create and initialize and instance of the PN532 class.
	pn532 = PN532.PN532(cs=CS, sclk=SCLK, mosi=MOSI, miso=MISO)
	pn532.begin()
	pn532.SAM_configuration()

	uid = pn532.read_passive_target()
	if (uid is not None):
		return '{0}' .format(binascii.hexlify(uid))

try:
	while(var == 0):
		card=reader()
		print(card)
		if card != None:
			username_req = urllib2.urlopen(ip + '/getinitialdata/' + card)
			username = username_req.read()
			print(username)
			direction_req = urllib2.urlopen(ip + '/nextdirection/' + str(0))
			direction = direction_req.read()
			print(direction)
			create_req = urllib2.urlopen(ip + '/createrecord/' + card + '/' + username + '/' + str(0) + '/' + direction)
			create = create_req.read()
			print(create)


except KeyboardInterrupt:
                GPIO.cleanup()

