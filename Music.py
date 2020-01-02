#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
import time

octave = 1

# region Notes Definition
# Source: https://pages.mtu.edu/~suits/notefreqs.html
C4 = 261.63
C4_Sh = D4_Fl = 277.18
D4 = 293.66
D4_Sh = E4_Fl = 311.13
E4 = 329.63
F4 = 349.23
F4_Sh = G4_Fl = 369.99
G4 = 392.00
G4_Sh = A4_Fl = 415.30
A4 = 440.00
A4_Sh = B4_Fl = 466.16
B4 = 493.88

C3 = C4 / 2
C3_Sh = D3_Fl = C4_Sh/2
D3 = D4 / 2
D3_Sh = E3_Fl = D4_Sh/2
E3 = E4 / 2
F3 = F4 / 2
F3_Sh = G3_Fl = F4_Sh/2
G3 = G4 / 2
G3_Sh = A3_Fl = G4_Sh/2
A3 = A4 / 2
A3_Sh = B3_Fl = A4_Sh/2
B3 = B4 / 2

C5 = C4 * 2
C5_Sh = D5_Fl = C4_Sh*2
D5 = D4 * 2
D5_Sh = E5_Fl = D4_Sh*2
E5 = E4 * 2
F5 = F4 * 2
F5_Sh = G5_Fl = F4_Sh*2
G5 = G4 * 2
G5_Sh = A5_Fl = G4_Sh*2
A5 = A4 * 2
A5_Sh = B5_Fl = A4_Sh*2
B5 = B4 * 2
# endregion Notes Definition


SongNotes = [B4,A4,A4_Fl,A4,C5,0,D4,C4,B4,C5,E5]
for i in SongNotes:
    if(i != 0):
        brick.sound.beep((i*octave), 150, 1)
    else:
        time.sleep(.2)

# Signalise end of Program
# time.sleep(3)
# brick.sound.beep()
# time.sleep(.1)
# brick.sound.beep()
# time.sleep(.1)
# brick.sound.beep()
