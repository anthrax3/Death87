"""
    Copyright 2015 Ricky LeDew

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

import pygame


class Particle(pygame.sprite.Sprite):
    def __init__(self, width, height, vx, vy, emitter, timeout, color, gravity):
        pygame.sprite.Sprite.__init__(self)
        self.pos = (emitter.rect.x + emitter.width/2, emitter.rect.y + emitter.height/2)
        self.width = width
        self.height = height
        self.vx = vx
        self.vy = vy
        self.emitter = emitter
        self.timeout = timeout
        self.color = color
        self.gravity = gravity
        self.shoulddie = False

        self.image = pygame.Surface((self.width, height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]

    def update(self):
        if self.timeout > 0:
            self.vy += self.gravity
            self.rect.x += self.vx
            self.rect.y += self.vy
            self.image.set_alpha(self.timeout)
            self.image.fill(self.color)
            self.timeout -= 1
        else:
            self.shoulddie = True