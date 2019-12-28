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

# Signalise start of Program
brick.sound.beep()
time.sleep(.1)


# region CODE
# region Definitions
# region Motors

CanonMotor = Motor(Port.A)
LeftFootMotor = Motor(Port.B)
RightFootMotor = Motor(Port.C)

# endregion Motors
# region Sensors
TouchSensor = TouchSensor(Port.S1)
ColorSensor = ColorSensor(Port.S3)
# UltrasonicSensor = UltrasonicSensor(Port.S4)
# endregion Sensors

# endregion Definitions

# robot = DriveBase(LeftFootMotor, RightFootMotor, 42, 160)
# drive = True
# while drive:
#     robot.drive(200, 0)
#     if ColorSensor.color() == Color.BLACK:
#         robot.drive_time(-100, 0, 2000)
#         robot.drive_time(0, 60, 2000)
#     wait(10)
#     if (TouchSensor.pressed()):
#         drive = False
#         robot.drive(0, 0)

# while ColorSensor.color() != Color.BLACK:
#     if not (TouchSensor.pressed()):
#         brick.display.image(ImageFile.WINKING)
#         brick.sound.file(SoundFile.BLUE)
#         brick.sound.file(SoundFile.GREEN)
# time.sleep(1)

while not (TouchSensor.pressed()):
    if (Button.CENTER in brick.buttons()):
        brick.sound.file(SoundFile.MOTOR_START)
    if (Button.LEFT in brick.buttons()):
        brick.sound.file(SoundFile.LEFT)
    if (Button.UP in brick.buttons()):
        brick.sound.file(SoundFile.UP)
    if (Button.RIGHT in brick.buttons()):
        brick.sound.file(SoundFile.RIGHT)
    if (Button.DOWN in brick.buttons()):
        brick.sound.file(SoundFile.DOWN)

# endregion CODE

# region Signalise end of Program
brick.sound.beep()
time.sleep(.1)
brick.sound.beep(1000)
time.sleep(.1)
brick.sound.beep()
# endregion Signalise end of Program
