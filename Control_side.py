import socket
from time import sleep
import curses
from pynput import keyboard

UDP_PORT = 5005
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.connect(("192.168.1.40", UDP_PORT))

damn = curses.initscr()
damn.nodelay(10)

base_speed = 30
# while True:
# 	c = damn.getch()
# 	if c == ord("w"):
# 		watchdog  = 1000
# 		data = '{} {}'.format(base_speed, base_speed)
# 	if c == ord("a"):
# 		data = '{} {}'.format(0, base_speed)
# 	if c == ord("d"):
# 		data = '{} {}'.format(base_speed, 0)
# 	if (c == -1) & (watchdog <= 0):
# 		data = '{} {}'.format(0, 0)


# 	sock.send(str.encode(data))
# 	# sleep(0.01)
# 	# print(data)
# 	watchdog -= 1

def on_press(key):
	try:
		control_key = key.char
	except AttributeError:
		print('special key {0} pressed'.format(key))
		control_key = "null"
	data = "0 0sock.send(str.encode(data))"
	if control_key == "w":
		data = '{} {}'.format(base_speed, base_speed)
	if control_key == "a":
		data = '{} {}'.format(0, base_speed)
	if control_key == "d":
		data = '{} {}'.format(base_speed, 0)
	sock.send(str.encode(data))

def on_release(key):
	sock.send(str.encode('{} {}'.format(0, 0)))
	if key == keyboard.Key.esc:
		return False

while True:
	# Collect events until released
	with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
		listener.join()




	# sock.send(str.encode(data))
	# sleep(0.01)
	# print(data)



