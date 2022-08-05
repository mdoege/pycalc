#!/usr/bin/env python

# Python scientific calculator

import pygame
from math import *

BACKGROUND = 0, 0, 0
BORDER = 6
RES = 760,600           # initial window size
HSIZE, VSIZE = 6, 9     # button grid dimension (top row is for display)
MAXLEN = 100            # maximum digits

# font name
fn = "Antonio-Regular.ttf"

# sound files
pygame.mixer.init()
audio = {
"key": pygame.mixer.Sound("key.wav"),
"enter": pygame.mixer.Sound("enter.wav"),
"clear": pygame.mixer.Sound("clear.wav"),
"error": pygame.mixer.Sound("error.wav"),
}

# button layout
bmap = """0x hex( oct( bin( **    C
          a  exp( sin( cos( tan(  log10(
          b  pi   abs( **2  sqrt( log(
          c  deg( SCI  (    )     /
          d  rad( 7    8    9     *
          e  fah( 4    5    6     -
          f  cel( 1    2    3     +
          0o 0b   0    .    j     ="""

# button text substitutions
subst = (
("/",   "DIV"),
("*",   "MUL"),
("-",   "SUB"),
("+",   "ADD"),
("=",   "ENTER"),
("**",  "POW"),
("**2", "SQ"),
("C",   "CLEAR"),
("j",   "IMAG"),
("(",   "BEGIN"),
(")",   "END"),
(".",   "SEP"),
)

# color indices for buttons
col_ind = """333312
311111
311111
311114
315554
315554
315554
335554"""

col_ind = col_ind.splitlines()

# RGB colors for each color index
cols = (
(255, 255, 255),
(204,153,204),
(255,153,0),
(204,102,102),
(153,153,255),
(255,153,102),
)

# highlight color
col_high = 255, 204, 153

# text colors and sizes
button_rgb  = 0, 0, 0
display_rgb = 255,153,0
size_button = 20
size_disp   = 55

but = []
for l in bmap.splitlines():
    bb = l.split()
    but.append(bb)

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
a = 0                 # last answer
b = 0                 # next-to-last answer
c = 299792458         # speed of light in m/s
d = 6.02214076e23     # Avogadro constant
                      # "e" is Euler's number 2.718…
f = 6.6743e-11        # gravitational constant in m³/(kg s)
j = 1.495978707e11    # astronomical unit (AU) in m

class PyCalc:
    def __init__(self):
        pygame.init()
        self.res = RES
        self.screen = pygame.display.set_mode(self.res, pygame.RESIZABLE)
        pygame.display.set_caption('PyCalc')
        self.screen.fill(BACKGROUND)
        self.font = pygame.font.Font(fn, size_button)
        self.fontres = pygame.font.Font(fn, size_disp)
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
                if ci == "=":       # evaluate expression
                    try:
                        self.inp = str(eval(self.inp))
                        b = a
                        a = eval(self.inp)
                        audio["enter"].play()
                    except:
                        self.inp += " *ERROR*"
                        audio["error"].play()
                elif ci == "C":     # clear screen
                    self.inp = ""
                    audio["clear"].play()
                elif ci == "SCI":   # convert to scientific notation
                    try:
                        self.inp = "%e" % float(self.inp)
                    except:
                        pass
                    audio["key"].play()
                else:               # or add button text to input
                    self.inp += but[Y - 1][X]
                    audio["key"].play()

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
        LCW = boxx // 6
        for y in range(1, VSIZE):
            for x in range(HSIZE):
                t = but[y - 1][x]
                ci = int(col_ind[y - 1][x])
                color = cols[ci]

                # check for matching parentheses:
                if t == ")":
                    par = self.inp.count("(") - self.inp.count(")")
                    if par > 0:
                        color = col_high

                pygame.draw.rect(self.screen, color,
                    [x * boxx + BORDER + LCW, y * boxy + BORDER,
                    boxx - 2 * BORDER - 2 * LCW, boxy - 2 * BORDER])
                pygame.draw.ellipse(self.screen, color,
                    (x * boxx + BORDER, y * boxy + BORDER, 2 * LCW, boxy - 2 * BORDER))
                pygame.draw.ellipse(self.screen, color,
                    (x * boxx - BORDER + boxx - 2 * LCW, y * boxy + BORDER, 2 * LCW, boxy - 2 * BORDER))
                if t[-1] == "(" and t != "(":
                    t = t[:-1]
                for a, b in subst:
                    if t == a: t = b
                if t != "#":
                    tr = self.font.render(t.upper(), True, button_rgb)
                    ox = max(0, boxx // 4)
                    oy = max(0, (boxy - tr.get_height()) // 2)
                    self.screen.blit(tr, (x * boxx + BORDER + ox, y * boxy + BORDER + oy))
        if len(self.inp) < MAXLEN:  # check if maximum digits exceeded
            t = self.inp
        else:
            try:
                self.inp = "%e" % float(self.inp)
                t = self.inp
            except:
                t = "*TOO LONG*"
        tr = self.fontres.render(t.upper(), True, display_rgb)
        self.screen.blit(tr, (10, 0))
        pygame.display.flip()

app = PyCalc()
app.run()

