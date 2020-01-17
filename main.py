#!/usr/bin/env pybricks-micropython

# region IMPORTS

from pybricks import ev3brick as brick
from pybricks.ev3devices import (
    Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (
    Port, Stop, Direction, Button, Color, SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import time
# endregion IMPORTS

# region Definitions
# region Motors

CanonMotor = Motor(Port.A)
LeftFootMotor = Motor(Port.B)
RightFootMotor = Motor(Port.C)

# endregion Motors
# region Sensors
TouchSensor = TouchSensor(Port.S1)
ColorSensor = ColorSensor(Port.S3)
IRSensor = InfraredSensor(Port.S4)
# endregion Sensors

robot = DriveBase(LeftFootMotor, RightFootMotor, 42, 160)

ShotsAvailable = 3

CurrentSpeed = 40

Volume = 5

# endregion Definitions


# Signalise start of Program
while (Button.CENTER not in brick.buttons()):
    wait(10)

brick.sound.file(SoundFile.START, Volume)
brick.display.image(ImageFile.EV3_ICON)
brick.sound.beep(500, 100, Volume)
wait(2000)

# region Functions


def DodgeManeuver():
    # brick.sound.file(SoundFile.TURN, Volume)
    brick.display.image(ImageFile.UP)
    robot.drive_time(-(CurrentSpeed/2), 0, 2000)
    robot.drive_time(0, 60, 2000)


def SlowDown():

    brick.display.image(ImageFile.ANGRY)
    robot.drive((CurrentSpeed/2), 0)
    brick.sound.file(SoundFile.SPEED_DOWN, Volume)
    while (IRSensor.distance() <= 40):
        if (IRSensor.distance() <= 20):
            DodgeManeuver()
        wait(10)
    robot.drive(CurrentSpeed, 0)
    brick.sound.file(SoundFile.SPEED_UP, Volume)


def Refill():
    robot.stop(Stop.HOLD)
    wait(100)
    while (not (Button.CENTER in brick.buttons())):
        wait(10)
    brick.sound.file(SoundFile.THANK_YOU, Volume)
    return 3


def Shoot(ShotsAvailable):
    robot.stop(Stop.HOLD)
    brick.sound.file(SoundFile.RED, Volume)
    brick.sound.file(SoundFile.DETECTED, Volume)
    brick.display.image(ImageFile.EVIL)
    wait(100)
    if (ShotsAvailable > 0):
        brick.sound.file(SoundFile.THREE, Volume)
        wait(500)
        brick.sound.file(SoundFile.TWO, Volume)
        wait(500)
        brick.sound.file(SoundFile.ONE, Volume)
        wait(500)
        brick.sound.file(SoundFile.ZERO, Volume)
        CanonMotor.run_angle(500, 1080)
        wait(500)
        ShotsAvailable -= 1
        if (ShotsAvailable == 2):
            brick.sound.file(SoundFile.TWO, Volume)
            brick.sound.file(SoundFile.READY, Volume)
        if (ShotsAvailable == 1):
            brick.sound.file(SoundFile.ONE, Volume)
            brick.sound.file(SoundFile.READY, Volume)
        if (ShotsAvailable == 0):
            brick.sound.file(SoundFile.ZERO, Volume)
            brick.sound.file(SoundFile.READY, Volume)
    else:
        brick.sound.file(SoundFile.UH_OH, Volume)
        brick.display.image(ImageFile.THUMBS_DOWN)
    wait(1500)
    return ShotsAvailable


# endregion Functions


# region CODE
# Initiate Start
drive = True

while drive:
    brick.display.image(ImageFile.AWAKE)
    robot.drive(CurrentSpeed, 0)
    if (IRSensor.distance() < 40):
        SlowDown()
    if (ColorSensor.color() == Color.GREEN):
        robot.stop(Stop.HOLD)
    if (ColorSensor.color() == Color.RED):
        ShotsAvailable = Shoot(ShotsAvailable)
    if (TouchSensor.pressed()):
        drive = False
        robot.stop(Stop.HOLD)
    if (Button.CENTER in brick.buttons()):
        ShotsAvailable = Refill()
    wait(10)

# endregion CODE

# region Signalise end of Program
brick.sound.file(SoundFile.STOP, Volume)
brick.display.image(ImageFile.SLEEPING)

brick.sound.beep(500, 100, Volume)
time.sleep(.1)
brick.sound.beep(500, 1000, Volume)
time.sleep(.1)
brick.sound.beep(500, 100, Volume)
# endregion Signalise end of Program
