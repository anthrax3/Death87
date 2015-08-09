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

class Groups:
    def __init__(self):
        self.visible = pygame.sprite.Group()
        self.sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.text = pygame.sprite.Group()
        self.particles = pygame.sprite.Group()
        self.emitters = pygame.sprite.Group()

    def addtogroup(self, object, group):
        group.add(object)