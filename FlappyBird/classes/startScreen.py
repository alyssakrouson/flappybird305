import button
import pygame

from pygame import *

class StartScreen():

    def __init__(self):

        self.clock = pygame.time.Clock()
        self.FPS = 60
        # Display + background initialization
        self.screen_w = 1000
        self.screen_h = 500
        self.bg_color = (0, 255, 0)
        self.screen = pygame.display.set_mode((self.screen_w, self.screen_h))
        self.bg = pygame.image.load('Background.jpg').convert()
        pygame.display.set_caption('Floating Fred')

        # loading button image
        strt_img = pygame.image.load('startbutton.png').convert_alpha()
        exit_img = pygame.image.load('exitbutton.png').convert_alpha()
        resume_img = pygame.image.load('resume button.png').convert_alpha()

        # create button
        self.strt_button = button.Button(445, 180, strt_img, 1.25)
        self.exit_button = button.Button(445, 280, exit_img, 1.25)
        self.resume_button = button.Button(445, 180, resume_img, 1.25)

        # define fonts
        self.font = pygame.font.SysFont("arialblack", 40)

        # define color
        self.TEXT_COL = (255, 255, 255)


    def draw_text(self, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        self.screen.blit(img, (x, y))


    def run_game(self):
        # game loop
        open = True
        # game variables
        import math
        game_paused = False
        bg_w = self.bg.get_width()
        tiles = math.ceil(self.screen_w / bg_w) + 1

        scroll = 0
        while open:

            self.clock.tick(self.FPS)

            for i in range(0, tiles):
                self.screen.blit(self.bg, (i * bg_w + scroll, 0))

            scroll -= 5

            if abs(scroll) > bg_w:
                scroll = 0

            # check if game is paused
            self.draw_text("Floating Fred", self.font, self.TEXT_COL, 365, 100)

            if game_paused == True:
                if self.exit_button.draw(self.screen):
                    open = False
                if self.resume_button.draw(self.screen):
                    game_paused = False
                # display the paused menu
            # else:
            # draw_text("Press P to pause", font, TEXT_COL, 150, 250)

            # button logic
            if game_paused == False:
                if self.strt_button.draw(self.screen):
                    return True
                if self.exit_button.draw(self.screen):
                    pygame.quit()
                    return False

            # event handler
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        game_paused = True
                if event.type == pygame.QUIT:
                    open = False

            pygame.display.update()