#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
import time

SongNotes = [246.94,220.00,207.65,220.00,261.63,261.63,0,293.66,261.63,246.94,261.63,329.63,0,0,349.23,329.63,311.13,329.63,493.88,440.00,415.30,440.00,493.88,440.00,415.30,440.00,523.25]
for i in SongNotes:
    if(i!=0):
        brick.sound.beep((i*2),150,1)
    else:
        time.sleep(.2)

# Signalise end of Program
# time.sleep(3)
# brick.sound.beep()
# time.sleep(.1)
# brick.sound.beep()
# time.sleep(.1)
# brick.sound.beep()
