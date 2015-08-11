# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#  ______   _______  _______ _________             _____   ______     #
#  (  __  \ (  ____ \(  ___  )\__   __/|\     /|   / ___ \ / ___  \   #
#  | (  \  )| (    \/| (   ) |   ) (   | )   ( |  ( (___) )\/   )  )  #
#  | |   ) || (__    | (___) |   | |   | (___) |   \     /     /  /   #
#  | |   | ||  __)   |  ___  |   | |   |  ___  |   / ___ \    /  /    #
#  | |   ) || (      | (   ) |   | |   | (   ) |  ( (   ) )  /  /     #
#  | (__/  )| (____/\| )   ( |   | |   | )   ( |  ( (___) ) /  /      #
#  (______/ (_______/|/     \|   )_(   |/     \|   \_____/  \_/       #
#                                                                     #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

import sys
from pygame.locals import *

from Scene import *




# Variable declaration
gameShouldClose = False
FPS = 60

pygame.init() # Initialize PyGame
window_class = Window()
window = window_class.createWindow(1000, 700)  # Create window
pygame.display.set_caption('Death 87')  # Set window title

fpsClock = pygame.time.Clock()
pygame.key.set_repeat(10, 10)

def getevents():
    for event in pygame.event.get():  # Handle Events
        global gameShouldClose
        pygame.display.update()
        if event.type == QUIT:
            gameShouldClose = True
        elif event.type == KEYDOWN or event.type == KEYUP:
            keys = pygame.key.get_pressed()
            if keys[K_ESCAPE]:
                gameShouldClose = True
            if keys[K_r]:
                scene.player.respawn()
            if keys[K_SPACE]:
                if scene.player.onTop:
                    scene.player.vy += -5
                elif scene.player.onBottom:
                    scene.player.vy += 3
                elif scene.player.onRight:
                    scene.player.vx += 3
                    scene.player.vy += -3
                elif scene.player.onLeft:
                    scene.player.vx += -3
                    scene.player.vx += 3

            if keys[K_LEFT]:
                if scene.player.onTop:
                    scene.player.vx += -2
                else:
                    scene.player.vx += -0.1
            if keys[K_RIGHT]:
                if scene.player.onTop:
                    scene.player.vx += 2
                else:
                    scene.player.vx += 0.1

scene = Scene(window_class, window, fpsClock)  # Load Scene
while not gameShouldClose: # game loop
    getevents()
    scene.update()

    # Graphics
    window.fill((0, 0, 0))
    scene.draw()

    fpsClock.tick(FPS)
    pygame.display.flip()


pygame.quit()
sys.exit(0)

