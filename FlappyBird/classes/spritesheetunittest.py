import unittest
import pygame
from spritesheet import Spritesheet

class SpritesheetTestCase(unittest.TestCase):
    screen_width = 1280
    screen_height = 720
    screen = pygame.display.set_mode((screen_width, screen_height))

    def setUp(self):
        self.sprite_sheet = Spritesheet('/Users/christopherlawler/Documents/CSC305/s23k/FlappyBird/Game_Sprites.png')

    def test_parse_sprite(self):
        r = pygame.Rect(450, 372, 80, 55)
        x, y, w, h = r

        sprite = self.sprite_sheet.parse_sprite('Bird_Idle.png')
        self.assertIsInstance(sprite, pygame.Surface)
        self.assertEqual(450, x, "Literal x value is not equal to x.")
        self.assertLess(y, 455, "Literal x value is not equal to y.")
        self.assertEqual(sprite.get_width(), w, "Literal width value is not equal to width.")
        self.assertEqual(sprite.get_height(), h, "Literal height value is not equal to height.")

if __name__ == '__main__':
    unittest.main()







