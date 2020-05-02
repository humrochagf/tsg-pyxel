import time
from collections import namedtuple

import pyxel

from .constants import PLAYER_SPEED

Sprite = namedtuple('Sprite', ['img', 'u', 'v', 'w', 'h', 'colkey'])


class Player:

    sprites = {
        'idle': [
            Sprite(0, 0, 0, 4, 7, pyxel.COLOR_BLACK),
        ],
        'up': [
            Sprite(0, 36, 0, 4, 7, pyxel.COLOR_BLACK),
            Sprite(0, 40, 0, 4, 7, pyxel.COLOR_BLACK),
        ],
        'down': [
            Sprite(0, 4, 0, 4, 7, pyxel.COLOR_BLACK),
            Sprite(0, 8, 0, 4, 7, pyxel.COLOR_BLACK),
        ],
        'left': [
            Sprite(0, 12, 0, 4, 7, pyxel.COLOR_BLACK),
            Sprite(0, 16, 0, 4, 7, pyxel.COLOR_BLACK),
            Sprite(0, 12, 0, 4, 7, pyxel.COLOR_BLACK),
            Sprite(0, 20, 0, 4, 7, pyxel.COLOR_BLACK),
        ],
        'right': [
            Sprite(0, 24, 0, 4, 7, pyxel.COLOR_BLACK),
            Sprite(0, 28, 0, 4, 7, pyxel.COLOR_BLACK),
            Sprite(0, 24, 0, 4, 7, pyxel.COLOR_BLACK),
            Sprite(0, 32, 0, 4, 7, pyxel.COLOR_BLACK),
        ],
    }

    def __init__(self, x, y):
        self.action = 'idle'

        self.x = x
        self.y = y

        self.vx = 0
        self.vy = 0

    def get_frame(self):
        frames = self.sprites[self.action]

        return frames[int((time.time() * 5) % len(frames))]

    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT):
            self.vx = -PLAYER_SPEED
        elif pyxel.btn(pyxel.KEY_RIGHT):
            self.vx = PLAYER_SPEED
        else:
            self.vx = 0

        if pyxel.btn(pyxel.KEY_DOWN):
            self.vy = PLAYER_SPEED
        elif pyxel.btn(pyxel.KEY_UP):
            self.vy = -PLAYER_SPEED
        else:
            self.vy = 0

        self.x += self.vx
        self.y += self.vy

        if self.vy > 0:
            self.action = 'down'
        elif self.vy < 0:
            self.action = 'up'
        elif self.vx < 0:
            self.action = 'left'
        elif self.vx > 0:
            self.action = 'right'
        else:
            self.action = 'idle'

    def draw(self):
        frame = self.get_frame()

        pyxel.blt(
            self.x,
            self.y,
            frame.img,
            frame.u,
            frame.v,
            frame.w,
            frame.h,
            frame.colkey,
        )
