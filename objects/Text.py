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


class Text(pygame.sprite.Sprite):
    def __init__(self, window, x, y, size, font, text, antialias, color):

        pygame.sprite.Sprite.__init__(self)
        self.window = window

        self.x = x
        self.y = y
        self.font = pygame.font.SysFont(font, size)
        self.text = text
        self.aa = antialias
        self.color = color
        self.image = pygame.Surface(self.font.size(self.text), pygame.SRCALPHA, 32)
        renderedfont = self.font.render(self.text, self.aa, self.color)
        self.image.blit(renderedfont, (0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.image = pygame.Surface(self.font.size(self.text), pygame.SRCALPHA, 32)
        renderedfont = self.font.render(self.text, self.aa, self.color)
        self.image.blit(renderedfont, (0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

