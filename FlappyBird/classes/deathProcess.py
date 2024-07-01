import pygame
from classes.spritesheet import Spritesheet
import random


class DeathProcess:
    def __init__(self, _screen):
        self.screen = _screen
        self.my_spritesheet = Spritesheet('Game_Sprites.png')
        self.bird_idle = self.my_spritesheet.parse_sprite('Bird_Idle.png')
        self.bird_dead = self.my_spritesheet.parse_sprite('Bird_Dead.png')
        self.bird_impacted = self.my_spritesheet.parse_sprite('Bird_Impacted.png')
        self.bird_sunglasses = self.my_spritesheet.parse_sprite('Sunglasses.png')
        pass

    def animate(self, birdX, birdY, FPS, displayPipe1, displayPipe2, drawOnScreen, backgroundColor):
        dt = FPS.render()
        glassesX = birdX + 23
        glassesY = birdY - 5
        glassesXSpeed = random.randint(-3, 3)
        glassesGrav = -3.6 * dt
        while glassesY < 500:
            dt = FPS.render()
            self.screen.fill(backgroundColor)
            displayPipe1.generatePipeGraphic(drawOnScreen)
            displayPipe2.generatePipeGraphic(drawOnScreen)
            self.screen.blit(self.bird_impacted, (birdX, birdY))
            glassesGrav += 0.3 * dt
            glassesX += glassesXSpeed
            glassesY = glassesY + glassesGrav
            self.screen.blit(self.bird_sunglasses, (glassesX, glassesY))
            pygame.display.update()
        while birdY < 416:
            self.screen.fill(backgroundColor)
            displayPipe1.generatePipeGraphic(drawOnScreen)
            displayPipe2.generatePipeGraphic(drawOnScreen)
            dt = FPS.render()
            birdY += 2.5 * dt
            self.screen.blit(self.bird_dead, (birdX, birdY))
            pygame.display.update()