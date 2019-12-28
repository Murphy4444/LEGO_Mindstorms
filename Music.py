#!/usr/bin/env pybricks-micropython
""" 
=== IMPORTS ===
"""
from pybricks import ev3brick as brick
from pybricks.ev3devices import (
    Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (
    Port, Stop, Direction, Button, Color, SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import time


# Signalise start of Program
brick.sound.beep()
time.sleep(.1)
""" 
=== CODE ===
"""


# Signalise end of Program
brick.sound.beep()
time.sleep(.1)
brick.sound.beep()
time.sleep(.1)
brick.sound.beep()
