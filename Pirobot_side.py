import socket
from RPi.GPIO import *
from time import sleep
import sys
import tty


UDP_PORT = 5005
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
sock.bind(('', UDP_PORT))


pwm1 = 37
pwm2 = 35

pwm3 = 38
pwm4 = 40

setmode(BOARD)

setup(pwm1,OUT)
setup(pwm2,OUT)
setup(pwm3,OUT)
setup(pwm4,OUT)

left_1 = PWM(pwm1,50)
left_2 = PWM(pwm2,50)
right_1 = PWM(pwm3,50)
right_2 = PWM(pwm4,50)

def motor_run(speed, side):
	if abs(direction) != 1:
		return 1
	speed_1 = -(speed - speed*(speed/abs(speed)))/2
	speed_2 = (speed + speed*(speed/abs(speed)))/2
	if side == 1:
		left_1.start(speed_1)
		left_2.start(speed_2)
	elif side == 2:
		right_1.start(speed_1)
		right_2.start(speed_2)


while True:
	data = sock.recv(1024)
	if not data:
		print("fail")
		motor_run(0, 1, 1)
		motor_run(0, 1, 2)
		print("lol")
		break
	try:
		sp = data.split(" ")
		sp1, sp2 = sp[0], sp[1]
		sp1, sp2 = int(sp1), int(sp2)
	except:
		sp1, sp2 = 0, 0 
	motor_run(sp1, 1, 1)
	motor_run(sp2, 1, 2)






sock.close()
