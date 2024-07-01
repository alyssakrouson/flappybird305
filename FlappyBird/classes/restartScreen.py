import pygame
from classes.startScreen import StartScreen
from classes.LeaderboardStorage import LeaderboardStorage
from classes.LeaderboardEntry import LeaderboardEntry

class RestartScreen:
    """
    The RestartScreen class is responsible for displaying a screen that prompts the user to restart the game
    after the player character dies. This screen should also allow the user to navigate back to the PlayScreen class.
    """

    def __init__(self, screen_manager, score):
        """
        Initializes the RestartScreen with the given screen_manager.

        :param screen_manager: The ScreenManager responsible for managing and displaying game screens.
        """
        self.screen_manager = screen_manager
        self.play_again_button = pygame.Rect(100, 200, 200, 50)
        self.menu_button = pygame.Rect(100, 300, 200, 50)
        self.getNickname = True
        self.LeaderboardStorage = LeaderboardStorage()
        self.score = score
        self.nickname = ""
        self.scoreSaved = False

    def show(self):
        """
        Displays the restart screen to the user.
        """
        screen = self.screen_manager.screen
        clock = pygame.time.Clock()
        # Clear the screen
        screen.fill((0, 0, 0))
        entry = self.LeaderboardStorage.ReadScore()
        if entry is not None:
            self.nickname = entry.nickname

        font = pygame.font.SysFont(None, 50)
        while self.getNickname:
            screen.fill((0, 0, 0))

            font = pygame.font.Font(None, 36)
            scoretext = font.render("Your score: " + str(self.score), True, (255, 255, 255))
            nickname = font.render("Enter nickname: ", True, (255, 255, 255))
            screen.blit(scoretext, (125, 165))
            screen.blit(nickname, (125, 205))
            if entry is not None:
                highscore = font.render("High Score: " + str(entry.score), True, (255, 255, 255))
                screen.blit(highscore, (125, 245))
            score = self.LeaderboardStorage.ReadScore()
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.getNickname = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.nickname = ""
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.getNickname = False
                    elif event.key == pygame.K_BACKSPACE:
                        self.nickname = self.nickname[:-1]
                    else:
                        if event.key is not pygame.K_SPACE:
                            self.nickname += event.unicode
                text_surf = font.render(self.nickname, True, (255, 255,255))
                screen.blit(text_surf, (325, 205))
                pygame.display.flip()
                #print(self.nickname)
        if not self.scoreSaved:
            if entry is not None:
               if entry.score < self.score:
                    entry.updateScore(self.score)
               if entry.nickname != self.nickname:
                   entry.updateNickname(self.nickname)
            if entry is None:
                entry = LeaderboardEntry(self.nickname, None, self.score)
            self.LeaderboardStorage.SaveScore(entry)
            self.scoreSaved = True

        screen.fill((0, 0, 0))
        # Draw "Play again" button
        pygame.draw.rect(screen, (255, 255, 255), self.play_again_button)
        font = pygame.font.Font(None, 36)
        playagain = font.render("Play again", True, (0, 0, 0))
        screen.blit(playagain, (125, 205))

        # Draw "Menu" button
        pygame.draw.rect(screen, (255, 255, 255), self.menu_button)
        menu = font.render("Menu", True, (0, 0, 0))
        screen.blit(menu, (155, 305))

        # Update the display
        pygame.display.flip()


    def handle_event(self, event):
        """
        Handles the given event, checking if the user has clicked on the "Play again" or "Menu" buttons.

        :param event: A pygame event to be processed.
        """
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.play_again_button.collidepoint(event.pos):
                self.reset_game()
            elif self.menu_button.collidepoint(event.pos):
                start = StartScreen()
                start.run_game()
                self.reset_game()

    def reset_game(self):
        """
        Resets the game state, including pipes, character position, and user's score.
        """
        from classes.playScreen import PlayScreen
        play_screen = PlayScreen(self.screen_manager)
        self.screen_manager.change_screen(play_screen)

    def navigate_to_play_screen(self):
        """
        Transitions to the PlayScreen.
        """
        from classes.playScreen import PlayScreen
        self.screen_manager.change_screen(PlayScreen(self.screen_manager))
