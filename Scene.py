"""
    Copyright (C) 2015 Ricky LeDew

    This file is part of Death 87.

    Death 87 is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Death 87 is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""

import json
import decimal
import random
from objects.Player import *
from objects.Wall import *
from objects.Text import *
from objects.Particle import *
from Window import *
from Groups import *


class Scene:

    def __init__(self, window_class, window, fpsclock):
        self.window_class = window_class
        self.window = window
        self.clock = fpsclock
        self.groups = Groups()
        self.fps = False
        self.fpsmeter = None
        self.player = Player(window_class, (450, 450), 10, 10, (0, 0), self.groups)
        self.deathscreen_ticker = 255
        self.groups.addtogroup(self.player, self.groups.sprites)
        with open('levels/lvl_1.json', 'r') as data_file:
            data = json.loads(data_file.read(), parse_float=decimal.Decimal)


        for object in data["scene"]["objects"]:
            try:
                if data["scene"]["objects"][object]["type"] == 'wall':

                        x = int(data["scene"]["objects"][object]["x"])
                        y = int(data["scene"]["objects"][object]["y"])
                        width = int(data["scene"]["objects"][object]["width"])
                        height = int(data["scene"]["objects"][object]["height"])
                        color = (
                            int(data["scene"]["objects"][object]["color"][0]),
                            int(data["scene"]["objects"][object]["color"][1]),
                            int(data["scene"]["objects"][object]["color"][2])
                        )
                        fric = float(data["scene"]["objects"][object]["friction"])
                        soft = bool(data["scene"]["objects"][object]["soft"])
                        emitter = bool(data["scene"]["objects"][object]["emitter"])
                        wall = Wall(x, y, width, height, color, fric, soft)
                        self.groups.addtogroup(wall, self.groups.walls)
                        if emitter:
                            self.groups.addtogroup(wall, self.groups.emitters)

                elif data["scene"]["objects"][object]["type"] == "text":
                    text = data["scene"]["objects"][object]["text"]
                    x = int(data["scene"]["objects"][object]["x"])
                    y = int(data["scene"]["objects"][object]["y"])
                    font = data["scene"]["objects"][object]["font"]
                    size = int(data["scene"]["objects"][object]["size"])
                    antialias = bool(data["scene"]["objects"][object]["antialias"])
                    color = (
                        int(data["scene"]["objects"][object]["color"][0]),
                        int(data["scene"]["objects"][object]["color"][1]),
                        int(data["scene"]["objects"][object]["color"][2])
                    )

                    textobj = Text(self.window, x, y, size, font, text, antialias, color)
                    self.groups.addtogroup(textobj, self.groups.text)
            except KeyError:
                print "Invalid configuration for " + object + ". Ignoring object and moving on."

        for property in data["scene"]["properties"]:
            try:
                if property == "music":
                    try:
                        music = pygame.mixer.Sound(data["scene"]["properties"]["music"])
                        music.play(-1, fade_ms=1000)
                    except:
                        print "Could not load music. Maybe you entered a value other than string?"
                elif property == "fps" and bool(data["scene"]["properties"]["fps"]):
                    self.fps = True
                    pos = (
                        int(data["scene"]["properties"]["fps_pos"][0]),
                        int(data["scene"]["properties"]["fps_pos"][1])
                    )
                    fpstext = str(self.clock.get_fps()) + " FPS"
                    self.fpsmeter = Text(self.window, pos[0], pos[1], 20, None, fpstext, True, (255, 255, 255))
                    self.groups.addtogroup(self.fpsmeter, self.groups.text)
            except KeyError:
                print "Invalid configuration for " + property + ". Ignoring property and moving on."


    def update(self):
        self.player.update()
        for object in self.groups.emitters:
            particle = Particle(10, 10, random.randrange(-1, 2), random.randrange(-5, -2), object, 50, (255, 255, 255), 0.1)
            self.groups.addtogroup(particle, self.groups.particles)
        for p in self.groups.particles:
            p.update()
            if p.shoulddie:
                p.kill()
        if self.fps:
            self.fpsmeter.text = str(round(self.clock.get_fps(), 2)) + " FPS"
            self.fpsmeter.update()

    def draw(self):

        if self.player.dead:
            self.player.kill()
            if self.deathscreen_ticker == 0:
                self.deathscreen_ticker = 255
            if self.deathscreen_ticker > 0:
                self.window.fill((self.deathscreen_ticker, 0, 0))
                self.deathscreen_ticker -= 5
            if self.deathscreen_ticker < 1:
                self.player.respawn()
                self.groups.addtogroup(self.player, self.groups.sprites)


        self.groups.text.draw(self.window)
        self.groups.walls.draw(self.window)
        self.groups.sprites.draw(self.window)
        self.groups.particles.draw(self.window)