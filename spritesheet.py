import pygame
import json

class Spritesheet():
    def __init__(self, filename):
        self.filename = filename.replace('png', 'json') # opens file
        self.spritesheet = pygame.image.load(filename).convert()
        self.meta_data = self.filename
        try:
            with open(self.meta_data) as f:
                self.data = json.load(f) # loads info from file
            f.close()
        except FileNotFoundError:
            print('File does not exist, you idiot.') # dumb idiot moment
    # ---------------------------------------------------------------------

    # - gets sprite from spritesheet using info from parse_sprite -
    def get_sprite(self, x, y, w, h):
        sprite = pygame.Surface((w, h))
        sprite.set_colorkey((0, 0, 0))
        sprite.blit(self.spritesheet, (0, 0), (x, y, w, h))
        return sprite
    # -------------------------------------------------------------

    # ------------------ parses info from metadata file ------------------
    def parse_sprite(self, name):
        sprite = self.data['frames'][name]['frame']
        x, y, w, h = sprite['x'], sprite['y'], sprite['w'], sprite['h']
        image = self.get_sprite(x, y, w, h)
        return pygame.transform.scale(image, (128, 128))
    # --------------------------------------------------------------------

