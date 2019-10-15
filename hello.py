#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


import os
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, MoveTank, MoveSteering
from ev3dev2.sensor.lego import GyroSensor, ColorSensor, TouchSensor
from ev3dev2.sensor import INPUT_1, INPUT_4
from ev3dev2.sound import Sound
from ev3dev2.button import Button 
from ev3dev2.led import Leds

from time import sleep

rs = 25 #Run_Speed
tls = 30 #Turn_LEFT_Speed
trs = 30 #Turn_RIGHT_Speed

ms = MoveSteering(OUTPUT_B, OUTPUT_C)
btn = Button()
sound = Sound()
ts = TouchSensor()
lml = LargeMotor(OUTPUT_B)
lmr = LargeMotor(OUTPUT_C)
mt = MoveTank(OUTPUT_B, OUTPUT_C)
gs = GyroSensor()
csl = ColorSensor(INPUT_1)
csr = ColorSensor(INPUT_4)


csl.mode = MODE_COL_REFLECT = 'COL-REFLECT'
csr.mode = MODE_COL_REFLECT = 'COL-REFLECT'

OPEN_path = "./OPEN"
GREEN_LIGHT_path = "./GREEN_LIGHT"
OPEN_BLING_path = "./OPEN_BLING_BLING"
# OPEN_RED_LIGHT_path = "/home/robot/WRO_water-car/OPEN_RED_LIGHT"
#RESTART_TRAFFIC_LIGHT_path = "/home/robot/WRO_water-car/RESTART_TRAFFIC_LIGHT"
RESTART_TRAFFIC_LIGHT_path = "./RESTART_TRAFFIC_LIGHT"
OPEN_GREEN_LIGHT_path = "./OPEN_GREEN_LIGHT"

os.system('setfont Lat15-TerminusBold14')

# 洗輪胎
'''
while True:
    if btn.check_buttons(buttons=['up']):
        mt.on(-50, -50)
    elif btn.check_buttons(buttons=['up']) == False:
        mt.off()
'''
'''
if os.path.isfile(RESTART_TRAFFIC_LIGHT_path):
#if os.path.isfile("./RESTART_TRAFFIC_LIGHT"):    
    print("Found")
    os.remove(RESTART_TRAFFIC_LIGHT_path)
else:
    print("Not found!")

if os.path.isfile(GREEN_LIGHT_path):
    os.remove(GREEN_LIGHT_path)

if os.path.isfile(OPEN_path):
    os.remove(OPEN_path)
'''
'''
if os.path.isfile(RESTART_TRAFFIC_LIGHT_path):
    print("TEST")
    os.remove(RESTART_TRAFFIC_LIGHT_path)
else:
    print("What's up????")    
'''

if os.path.isfile(RESTART_TRAFFIC_LIGHT_path):
    os.remove(RESTART_TRAFFIC_LIGHT_path)

if os.path.isfile(OPEN_path):
    os.remove(OPEN_path)

if os.path.isfile(OPEN_BLING_path):
    os.remove(OPEN_BLING_path)

if os.path.isfile(OPEN_GREEN_LIGHT_path):
    os.remove(OPEN_GREEN_LIGHT_path)

if os.path.isfile(GREEN_LIGHT_path):
    os.remove(GREEN_LIGHT_path)







sound.speak("O, A, O, A")

print("OKOKOKOKOKOKOKOKOKOKOK")
'''
while True:
    if ts.is_pressed:
        mt.off()
        break
    if btn.check_buttons(buttons=['up']):
        mt.on(-50, -50)
    elif btn.check_buttons(buttons=['up']) == False:
        mt.off()
'''
ts.wait_for_bump()
sound.play_tone(2500, 0.1) 





os.system("echo 0 > RESTART_TRAFFIC_LIGHT")
print("RESTART_TRAFFIC_LIGHT")


'''
sleep(0.1)
os.system("echo 0 > RESTART_TRAFFIC_LIGHT")


sleep(2)

os.system("echo 0 > RESTART_TRAFFIC_LIGHT")
sleep(0.1)
os.system("echo 0 > RESTART_TRAFFIC_LIGHT")
sleep(0.1)
'''



mt.on(10.15, 10)

while True:
    #print(csr.color_name)
    #if csr.color_name == "White":
    if csr.reflected_light_intensity > 39:
        mt.off()
        break
       
    sleep(0.1)

lml.reset()
lmr.reset()
mt.on(10.1, 10)

while True:
    if lml.position > 328 or lmr.position > 328: #299
        mt.off()
        break
    sleep(0.1)

lml.reset()
lmr.reset()

if os.path.isfile(GREEN_LIGHT_path):
    os.remove(GREEN_LIGHT_path)
if os.path.isfile(GREEN_LIGHT_path):
    print('Clean GREEN_LIGHT')
    os.remove(GREEN_LIGHT_path)
# 第一個右彎
ms.on_for_rotations(50, 100, 1) # gs.angle > 76, 1.08
ms.wait_until_not_moving()



# 2



mt.on(rs+0.2, rs)
while True:
    if csl.reflected_light_intensity > 39 or csr.reflected_light_intensity > 39:
        mt.off()
        break
'''
if os.path.isfile(RESTART_TRAFFIC_LIGHT_path):
    os.remove(RESTART_TRAFFIC_LIGHT_path)
'''


# sleep(5)





while True:
    if os.path.isfile(GREEN_LIGHT_path) or ts.is_pressed:
        os.system("echo 0 > OPEN")
        sound.play_tone(2500, 0.1) 
        mt.off()
        sleep(1.5)
        break
    sleep(0.1)

lml.reset()
lmr.reset()

sleep(0.1)

mt.on(8.1, 8)

while True:
    if lml.position > 299 or lmr.position > 299:
        mt.off()
        break
    sleep(0.1)

mt.on(0, trs)

gs.mode = 'GYRO-RATE'
gs.mode = 'GYRO-ANG'

#紅綠燈前左彎
while True:
    lml.off()
    if gs.angle < -40 :
        mt.off()
        break
    sleep(0.1)

lmr.reset()
lml.reset()

mt.on(10.6, 10.5)

while True:
    if lml.position > 557 or lmr.position > 557:
        mt.off()
        break
    sleep(0.1)

sleep(0.1)



ms.on_for_rotations(-51, 100, 1.22) # gs.angle < -81
ms.wait_until_not_moving()



# 3



mt.on(15+0.2, 15)

while True:
    if csr.reflected_light_intensity > 39 or csl.reflected_light_intensity > 39:
        mt.off()
        break
    sleep(0.1)

if os.path.isfile(OPEN_path):
    os.remove(OPEN_path)

lml.reset()
lmr.reset()

mt.on(10.1, 10)

while True:
    if lml.position > 315 or lmr.position > 315:
        mt.off()
        break
    sleep(0.1)

sleep(0.1)
gs.mode = 'GYRO-RATE'
gs.mode = 'GYRO-ANG'
mt.on(0, trs * 2.5)
while True:
    lml.off()
    if gs.angle < -50:
        mt.off()
        break
    sleep(0.1)

mt.on(20+0.2, 20)

sleep(0.1)



lml.reset()
lmr.reset()

mt.on(15+0.2, 15)

os.system("echo 0 > OPEN_BLING_BLING")
while True:
    if csl.color_name == "Yellow" and csr.color_name == "Yellow": # position > 1735
        mt.off()
        sleep(0.3)
        mt.on_for_rotations(rs, rs, 1.15)
        mt.wait_until_not_moving()

        break
    sleep(0.1)



sound.speak("O, K")
# END