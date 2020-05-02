from pathlib import Path

import pyxel

from .constants import GAME_HEIGHT, GAME_TITLE, GAME_WIDTH
from .player import Player


class Game:

    def __init__(self):
        pyxel.init(GAME_WIDTH, GAME_HEIGHT, caption=GAME_TITLE)

        pyxel.load(
            Path(__file__).resolve().parent / 'assets' / 'assets.pyxres'
        )

        self.player = Player(38, 36)

        pyxel.run(self.update, self.draw)

    def update(self):
        self.player.update()

    def draw(self):
        pyxel.cls(pyxel.COLOR_BLACK)

        self.player.draw()
