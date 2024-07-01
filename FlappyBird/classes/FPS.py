import pygame
import sys

class FramesPerSecond:
    def __init__(self) -> None:
        self.clock = pygame.time.Clock()
        
    def render(self) -> int:
        dt = self.clock.tick(40)
        dt /= 10
        return dt

