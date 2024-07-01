import pygame
import json

#https://github.com/ChristianD37/YoutubeTutorials/blob/master/spritesheet/spritesheet.py

class Spritesheet:

    # This __init__ constructor defines the filename that will be used for the .png file containing all sprites.
    # It also contains a sprite_sheet variable that converts the filename into the same pixel format as the display.
    # The meta_data variable uses values from the .json file in conjunction with the sprites from the .png.
    # The "with open()" function loads the .json values into the self.data variable.
    def __init__(self, filename):
        self.filename = filename
        self.sprite_sheet = pygame.image.load(filename)
        self.meta_data = filename.replace('.png', '.json')
        with open(self.meta_data) as f:
            self.data = json.load(f)

    # The get_sprite function extracts each sprite from the sprite sheet and the pygame.SRCALPHA pygame function
    # makes the black screen behind the sprites transparent.
    def get_sprite(self, x, y, w, h):
        sprite = pygame.Surface([w, h], pygame.SRCALPHA)
        sprite.blit(self.sprite_sheet, (0, 0), (x, y, w, h))
        return sprite

    # The parse_sprite function outputs the sprite values from the .json file and returns a sprite_image using those
    # set values.
    def parse_sprite(self, name):
        sprite_data = self.data['frames'][name]['frame']
        x, y, w, h = sprite_data["x"], sprite_data["y"], sprite_data["w"], sprite_data["h"]
        sprite_image = self.get_sprite(x, y, w, h)
        return sprite_image
