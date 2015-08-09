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


class Wall(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, color, dampening, friction, soft):

        pygame.sprite.Sprite.__init__(self)
        self.color = color
        self.dampening = dampening
        self.friction = friction
        self.image = pygame.Surface((width, height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()  # That's right, get rect!
        self.rect.x = x
        self.rect.y = y
        self.soft = soft