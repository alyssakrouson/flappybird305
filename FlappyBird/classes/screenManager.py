import pygame

class ScreenManager:
    def __init__(self, screen):
        self.screen = screen
        self.current_screen = None
        self.running = True

    def change_screen(self, screen):
        self.current_screen = screen

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                else:
                    self.current_screen.handle_event(event)
            self.current_screen.show()
            pygame.display.update()

        pygame.quit()
