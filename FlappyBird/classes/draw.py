import pygame
from classes.spritesheet import Spritesheet


class Draw():
    # Takes in screen to draw on in function call, the below functions draw rectangles (place holders)
    # only one method draws background in order to avoid drawing over objects/entities
    def __init__(self, _screen, backgroundColor):
        self.screen = _screen
        self.backgroundColor = backgroundColor
        self.screen.fill(self.backgroundColor)
        self.my_spritesheet = Spritesheet('Game_Sprites.png')
        self.bird_idle = self.my_spritesheet.parse_sprite('Bird_Idle.png')
        self.bird_dead = self.my_spritesheet.parse_sprite('Bird_Dead.png')
        self.bird_impacted = self.my_spritesheet.parse_sprite('Bird_Impacted.png')
        self.bird_sunglasses = self.my_spritesheet.parse_sprite('Sunglasses.png')
        self.pipe = self.my_spritesheet.parse_sprite('Pipe.png')
        self.upside_down_pipe = pygame.transform.rotate(self.pipe, 180)
        self.ground = self.my_spritesheet.parse_sprite('Ground.png')

    def drawBird(self):
        self.screen.blit(self.bird_idle, (self.birdX, self.birdY))

    def drawObstacle(self, obstacleX, screenY, gapPos) -> None:
        self.screen.blit(self.pipe, (obstacleX, screenY - 225 + gapPos))
        self.screen.blit(self.upside_down_pipe, (obstacleX, screenY - 750 + gapPos))

    def drawGround(self, movement, screenY):
        for i in range(26):
            self.screen.blit(self.ground, ((80 * i + movement) - 5, screenY - 45))

    def drawGlasses(self, glassesX, glassesY):
        self.screen.blit(self.bird_sunglasses, (glassesX, glassesY))