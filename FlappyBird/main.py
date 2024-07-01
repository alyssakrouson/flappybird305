import pygame
from classes.startScreen import StartScreen
from classes.playScreen import PlayScreen
from classes.screenManager import ScreenManager

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_manager = ScreenManager(screen)
playScreen = PlayScreen(screen_manager)
start = StartScreen()
cont = start.run_game()
if cont:
    screen_manager.change_screen(playScreen)

    screen_manager.run()
pygame.quit()