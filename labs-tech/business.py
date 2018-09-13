from controlLed import turn_on_led
from controlLed import turn_off_led
from readConfig import read

def controlLed(device, value):
	mapping = read()
	number = mapping[device]

	if value == 'on':
		turn_on_led(number)
	elif value == 'off':
		turn_off_led(number)
