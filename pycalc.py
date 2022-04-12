#!/usr/bin/env python

# Python calculator

import pygame
from math import *

BACKGROUND = 0, 0, 0
BORDER = 2
RES = 600,495           # initial window size
HSIZE, VSIZE = 6, 9     # button grid dimension
MAXLEN = 100            # maximum digits

# font name
fn = "OCRA.otf"

# button layout
bmap = """0x hex( oct( bin( ** C
a exp( sin( cos( tan( log10(
b pi abs( **2 sqrt( log(
c deg( SCI ( ) /
d rad( 7 8 9 *
e fah( 4 5 6 -
f cel( 1 2 3 +
0o 0b 0 . j ="""

# color indices
col_ind="""333312
311111
311111
311114
315554
315554
315554
335554"""

col_ind = col_ind.splitlines()

# RGB colors
cols = (
(0,0,0),
(100,100,100),
(50,0,0),
(0,50,0),
(0,30,50),
(130,130,130),
)

but = []
for l in bmap.splitlines():
    bb = l.split()
    but.append(bb)

#print(but)

def deg(x):
    return degrees(x)

def rad(x):
    return radians(x)

def fah(x):
    # Celsius -> Fahrenheit
    return (x * 9/5) + 32

def cel(x):
    # Fahrenheit -> Celsius
    return (x - 32) * 5/9

# Some predefined variables and constants:
#  (e is defined in math module)
a = 0     # last answer
b = 0     # next to last answer
c = 299792458   # speed of light in m/s
d = 6.02214076e23 # Avogadro constant
# e is Euler's number 2.718…
f = 6.6743e-11  # gravitational constant in m³/(kg s)
j = 1.495978707e11    # astronomical unit (AU) in m

class PyCalc:
    def __init__(self):
        pygame.init()
        self.res = RES
        self.screen = pygame.display.set_mode(self.res, pygame.RESIZABLE)
        pygame.display.set_caption('PyCalc')
        self.screen.fill(BACKGROUND)
        self.font = pygame.font.Font(fn, 25)
        self.fontres = pygame.font.Font(fn, 45)
        self.clock = pygame.time.Clock()
        self.inp = ""

    def events(self):
        global a, b

        for event in pygame.event.get():
            if event.type == pygame.QUIT: self.running = False
            if event.type == pygame.VIDEORESIZE:
                self.res = event.w, event.h
                self.last = 0
                self.screen = pygame.display.set_mode(self.res, pygame.RESIZABLE)
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                boxx, boxy = self.res[0] // HSIZE, self.res[1] // VSIZE
                X, Y = x // boxx, y // boxy
                if Y == 0 or Y > VSIZE - 1 or X > HSIZE - 1:
                    return
                ci = but[Y - 1][X]
                if ci == "=":
                    try:
                        self.inp = str(eval(self.inp))
                        b = a
                        a = eval(self.inp)
                    except:
                        self.inp += " *ERROR*"
                elif ci == "C":
                    self.inp = ""
                elif ci == "SCI":
                    try:
                        self.inp = "%e" % float(self.inp)
                    except:
                        pass
                else:
                    self.inp += but[Y - 1][X]

    def run(self):
        self.running = True
        while self.running:
            self.clock.tick(10)
            self.events()
            self.update()
        pygame.quit()

    def update(self):
        self.screen.fill(BACKGROUND)
        boxx, boxy = self.res[0] // HSIZE, self.res[1] // VSIZE
        for y in range(1, VSIZE):
            for x in range(HSIZE):
                ci = int(col_ind[y - 1][x])
                pygame.draw.rect(self.screen, cols[ci],
                    [x * boxx + BORDER, y * boxy + BORDER,
                    boxx - 2 * BORDER, boxy - 2 * BORDER])
                t = but[y - 1][x]
                if t[-1] == "(" and t != "(":
                    t = t[:-1]
                if t != "#":
                    tr = self.font.render(t, True, (255, 255, 255))
                    ox = max(0, (boxx - tr.get_width()) // 2)
                    oy = max(0, (boxy - tr.get_height()) // 2)
                    self.screen.blit(tr, (x * boxx + BORDER + ox, y * boxy + BORDER + oy))
        if len(self.inp) < MAXLEN:
            t = self.inp
        else:
            try:
                self.inp = "%e" % float(self.inp)
                t = self.inp
            except:
                t = "*TOO LONG*"
        tr = self.fontres.render(t, True, (255, 255, 0))
        self.screen.blit(tr, (0, 0))
        pygame.display.flip()

app = PyCalc()
app.run()

