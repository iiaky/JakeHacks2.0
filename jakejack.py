import pygame
from spritesheet import Spritesheet

class Jake(object):
    def __init__(self):

        # ------ movement controls ------
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.airborne = False

        self.move_x = 5
        self.move_y = 20
        self.gravity = 3

        self.x, self.y = [450, 350]
        self.location = [self.x, self.y]
        # -------------------------------

        self.hitbox = pygame.Rect(self.x, self.y, 110, 110)

        # -------------------- creates frames --------------------
        my_spritesheet = Spritesheet('assets/ssanimation.png')
        self.jake_ss = [my_spritesheet.parse_sprite('jake1.png'),
                        my_spritesheet.parse_sprite('jake2.png'),
                        my_spritesheet.parse_sprite('jake3.png'),
                        my_spritesheet.parse_sprite('jake4.png'),
                        my_spritesheet.parse_sprite('jake5.png'),
                        my_spritesheet.parse_sprite('jake6.png'),
                        my_spritesheet.parse_sprite('jake7.png')]
        # ----------------------------------------------------------

    def movement(self):
        if self.moving_right:
            self.location[0] += self.move_x
        if self.moving_left:
            self.location[0] -= self.move_x
        if self.moving_up:
            if self.airborne:
                return
            else:
                self.move_y -= 1
                self.location[1] -= self.move_y
        if self.moving_down:
            self.location[1] += self.move_y

        # -- gravity thing --
        if (self.airborne == False and self.moving_up == False and self.moving_down == False):
            if self.location[1] < 400:
                self.location[1] += self.gravity
        # -------------------