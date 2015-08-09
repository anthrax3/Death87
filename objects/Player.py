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
import math


class Player(pygame.sprite.Sprite):
    def __init__(self, window, pos, width, height, velocity, group):

        pygame.sprite.Sprite.__init__(self)

        self.width = width
        self.height = height
        self.origin = pos
        self.vx = velocity[0]
        self.vy = velocity[1]

        self.onRight = False
        self.onLeft = False
        self.onBottom = False
        self.onTop = False

        self.dead = False

        self.groups = group
        self.window = window

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()  # get rect!
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def respawn(self):
        self.rect.x = self.origin[0]
        self.rect.y = self.origin[1]
        self.vx = 0
        self.vy = 0
        self.dead = False

    def update(self):
        self.vy += 0.3


        self.onTop = False
        self.onBottom = False
        self.onRight = False
        self.onLeft = False
        self.rect.x += self.vx
        wallcollisons = pygame.sprite.spritecollide(self, self.groups.walls, False)
        for wall in wallcollisons:
            if self.vx > 0:
               # if (self.rect.right )
                if self.vx >= 15 and not wall.soft:
                    self.dead = True
                self.rect.right = wall.rect.left - 1
                self.vx = -self.vx * (1 - wall.dampening)
                self.vy = self.vy * (1 - wall.friction)
                self.onLeft = True
            else:
                if self.vx <= -15 and not wall.soft:
                    self.dead = True
                self.rect.left = wall.rect.right + 1
                self.vx = -self.vx * (1 - wall.dampening)
                self.vy = self.vy * (1 - wall.friction)
                self.onRight = True

        self.rect.y += self.vy

        wallcollisions = pygame.sprite.spritecollide(self, self.groups.walls, False)
        for wall in wallcollisions:
            if self.vy > 0:
                if self.vy >= 15 and not wall.soft:
                    self.dead = True
                self.rect.bottom = wall.rect.top
                self.vy = -self.vy * (1 - wall.dampening)
                self.vx = self.vx * (1 - wall.friction)
                self.onTop = True

            else:
                if self.vy <= -15 and not wall.soft:
                    self.dead = True
                self.rect.top = wall.rect.bottom
                self.vy = -self.vy * (1 - wall.dampening)
                self.vx = self.vx * (1 - wall.friction)
                self.onBottom = True


        if self.rect.x > self.window.windowWidth or self.rect.x < 0 or self.rect.y > self.window.windowHeight:
            self.dead = True
