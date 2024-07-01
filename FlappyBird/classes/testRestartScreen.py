import unittest
from unittest.mock import MagicMock
from unittest.mock import call
import pygame
from screenManager import ScreenManager
from restartScreen import RestartScreen
from playScreen import PlayScreen

class MockScreenManager(ScreenManager):
    def __init__(self):
        super().__init__()
        self.changed_screen = None

    def change_screen(self, screen):
        self.changed_screen = screen

class TestRestartScreen(unittest.TestCase):
    def setUp(self):
        self.mock_screen_manager = MockScreenManager()
        self.restart_screen = RestartScreen(self.mock_screen_manager)

    def test_navigate_to_play_screen(self):
        """
        Test if the navigate_to_play_screen() method correctly changes the screen to PlayScreen.
        """
        self.restart_screen.navigate_to_play_screen()
        self.assertIsInstance(self.mock_screen_manager.changed_screen, PlayScreen)

    def test_handle_event_play_again_button(self):
        """
        Test if the handle_event() method calls reset_game() when the play_again_button is clicked.
        """
        mock_event = MagicMock()
        mock_event.type = pygame.MOUSEBUTTONDOWN
        mock_event.button = 1
        mock_event.pos = (150, 225)  # Inside the play_again_button

        self.restart_screen.reset_game = MagicMock()
        self.restart_screen.handle_event(mock_event)

        self.restart_screen.reset_game.assert_called_once()

    def test_handle_event_menu_button(self):
        """
        Test if the handle_event() method calls navigate_to_play_screen() when the menu_button is clicked.
        """
        mock_event = MagicMock()
        mock_event.type = pygame.MOUSEBUTTONDOWN
        mock_event.button = 1
        mock_event.pos = (150, 325)  # Inside the menu_button

        self.restart_screen.navigate_to_play_screen = MagicMock()
        self.restart_screen.handle_event(mock_event)

        self.restart_screen.navigate_to_play_screen.assert_called_once()

if __name__ == '__main__':
    unittest.main()
