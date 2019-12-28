#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (
    Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (
    Port, Stop, Direction, Button, Color, SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase


TouchSensor = TouchSensor(Port.S1)
ColorSensor = ColorSensor(Port.S3)
# UltrasonicSensor = UltrasonicSensor(Port.S4)


CanonMotor = Motor(Port.A)
LeftFootMotor = Motor(Port.B)
RightFootMotor = Motor(Port.C)


robot = DriveBase(LeftFootMotor, RightFootMotor, 42, 160)

while True:
    robot.drive(200, 0)
    while not TouchSensor.pressed() and ColorSensor.color() != Color.BLACK :
        wait(10)
    
    robot.drive_time(-100, 0, 2000)

    robot.drive_time(0, 60, 2000)


RightFootMotor.run_target(500, 340)