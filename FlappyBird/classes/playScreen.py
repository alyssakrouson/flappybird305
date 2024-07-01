import pygame
import random
from classes.spritesheet import Spritesheet
from classes.draw import Draw
from classes.gravity import Gravity
from classes.FPS import FramesPerSecond
from classes.fly import Fly
from classes.pipe import Pipe
from classes.playerLifeState import playerLifeState
from classes.deathProcess import DeathProcess
from classes.restartScreen import RestartScreen
from classes.startScreen import StartScreen


class PlayScreen:
    def __init__(self, screen_manager):
        self.screen_manager = screen_manager
        self.screen = screen_manager.screen

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                newGravity = playerFlight.fly(birdY, dt, newGravity)
            if event.key == pygame.K_ESCAPE:
                self.screen_manager.running = False

    def countdown(self, text, font, displayGround, drawOnScreen):
        self.screen.fill(self.backgroundColor)
        self.screen.blit(self.Bird_Idle, (50, 100))
        displayGround.generatePipeGraphic(drawOnScreen)
        img = font.render(text, True, (0, 0, 0))
        self.screen.blit(img, (500, 100))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
        pygame.display.update()
        pygame.time.wait(700)


    def show(self):
        pygame.init()

        SCREEN_WIDTH = 1000
        SCREEN_HEIGHT = 500
        birdX = 50
        birdY = 100

        playerFlight = Fly()
        FPS = FramesPerSecond()
        playerGravity = Gravity()
        obstacleX = SCREEN_WIDTH - 100
        obstacleY = SCREEN_HEIGHT
        newGravity = 0
        score = 0
        self.backgroundColor = (173, 216, 230)
        birdLifeState = playerLifeState(birdX)
        drawOnScreen = Draw(self.screen, self.backgroundColor)
        nameList = ["Flying Fred", "Bouncy Flier", "Aviation Avian", "Jumpy Jay",
                    "Hoppy Fowl", "Cool Chick", "Flippy Fool", "Fine Feathered Friend",
                    "Mega Jump Death Trials", "Floaty Fluff", "Pipe Bird"]
        gameName = nameList[random.randint(0, 10)]
        pygame.display.set_caption(gameName)

        displayPipe1 = Pipe(SCREEN_HEIGHT, SCREEN_WIDTH)
        displayPipe2 = Pipe(SCREEN_HEIGHT, SCREEN_WIDTH + 525)

        sprite_sheet_image = pygame.image.load('Game_Sprites.png').convert_alpha()
        my_spritesheet = Spritesheet('Game_Sprites.png')
        self.Bird_Idle = my_spritesheet.parse_sprite('Bird_Idle.png')
        bird_dead = my_spritesheet.parse_sprite('Bird_Dead.png')
        bird_impacted = my_spritesheet.parse_sprite('Bird_Impacted.png')
        isAlive = True
        font = pygame.font.SysFont("arialblack", 100)
        self.countdown("3", font, displayPipe1, drawOnScreen)
        self.countdown("2", font, displayPipe1, drawOnScreen)
        self.countdown("GO!", font, displayPipe1, drawOnScreen)
        FPS.render()
        self.run = True
        while self.run:

            dt = FPS.render()
            if isAlive:
                # update background
                self.screen.fill(self.backgroundColor)

                # pipe movement
                displayPipe1.generatePipeGraphic(drawOnScreen)
                displayPipe1.moveGraphic(dt)
                displayPipe2.generatePipeGraphic(drawOnScreen)
                displayPipe2.moveGraphic(dt)
                self.screen.blit(self.Bird_Idle, (birdX, birdY))
                if displayPipe1.resetGraphic():
                    score += 1
                if displayPipe2.resetGraphic():
                    score += 1

                # calculate gravity
                birdY, newGravity = playerGravity.gravityEffect(birdY, dt, newGravity)

            isAlive = birdLifeState.evaluateState(birdY, displayPipe1.pipeX, displayPipe1.gapStartStop)
            if isAlive:
                isAlive = birdLifeState.evaluateState(birdY, displayPipe2.pipeX, displayPipe2.gapStartStop)
            if isAlive == False:

                birdDeath = DeathProcess(self.screen)
                birdDeath.animate(birdX, birdY, FPS, displayPipe1, displayPipe2, drawOnScreen, self.backgroundColor)

                # Change to the restart screen
                self.screen_manager.change_screen(RestartScreen(self.screen_manager, score))
                self.run = False





            # TO-DO: redraw background in Draw class to give the illusion of the player falling
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    pygame.quit()

                # Checks for pressed keys then adjusts character coords based on pressed keys
                keys = pygame.key.get_pressed()
                if keys[pygame.K_UP] or keys[pygame.K_SPACE]:
                    newGravity = playerFlight.fly(birdY, dt, newGravity)
                if keys[pygame.K_ESCAPE]:
                    pygame.quit()

            pygame.display.update()



