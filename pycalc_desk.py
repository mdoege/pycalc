#!/usr/bin/env python

# Python decimal desktop-style calculator

import pygame
from decimal import *

getcontext().prec = 10

BACKGROUND = 255, 255, 255
BORDER = 2
RES = 800,600           # initial window size
HSIZE, VSIZE = 4, 6     # button grid dimension (top row is for display)
MAXLEN = 100            # maximum digits

# font names
fn = "Federation.ttf"
fndis = "digital-7 (mono italic).ttf"

# button layout
bmap = """C    M+   MR    /
          7    8    9     *
          4    5    6     -
          1    2    3     +
          AC   0    .     ="""

# color indices for buttons
col_ind = """5555
1111
2222
3333
4444"""

col_ind = col_ind.splitlines()

# RGB colors for each color index
cols = (
(255, 255, 255),
(55, 150, 200),
(110, 220, 120),
(245, 220, 60),
(245, 150, 145),
(155, 140, 210),
)

# text colors and sizes
button_rgb  = 0, 0, 0
display_rgb = 0, 0, 0
size_button = 50
size_disp   = 100

but = []
for l in bmap.splitlines():
    bb = l.split()
    but.append(bb)


def to_dec(x):
    "Convert input to use Decimal class"

    s = x + " "
    o = ""
    num = ""
    for n in range(len(s)):
        if s[n] in "1234567890.":
            num += s[n]
        else:
            if num:
                o += f"Decimal('{num}')"
            num = ""
            o += s[n]
    return o

class PyCalc:
    def __init__(self):
        pygame.init()
        self.res = RES
        self.screen = pygame.display.set_mode(self.res, pygame.RESIZABLE)
        pygame.display.set_caption('PyCalc (decimal)')
        self.screen.fill(BACKGROUND)
        self.font = pygame.font.Font(fn, size_button)
        self.fontres = pygame.font.Font(fndis, size_disp)
        self.clock = pygame.time.Clock()
        self.inp = ""
        self.memory = 0

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
                        # first strip and then add decimal separators:
                        self.inp = f"{eval(to_dec(self.inp.replace(',', ''))):,}"
                    except:
                        #raise
                        self.inp += " *ERROR*"
                elif ci == "C":     # clear screen
                    self.inp = ""
                elif ci == "AC":    # all clear
                    self.inp = ""
                    self.memory = 0
                elif ci == "M+":    # add to memory
                    self.memory += eval(to_dec(self.inp.replace(',', '')))
                    self.inp += f"#{str(self.memory)}"
                elif ci == "MR":    # recall memory
                    self.inp += str(self.memory)
                else:               # or add button text to input
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
                    tr = self.font.render(t, True, button_rgb)
                    ox = max(0, (boxx - tr.get_width()) // 2)
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
        tr = self.fontres.render(t, True, display_rgb)
        self.screen.blit(tr, (20, 0))
        pygame.display.flip()

app = PyCalc()
app.run()

