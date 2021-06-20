import pygame
from jakejack import Jake
from screenevents import screening
from random import randint
pygame.init()

running = True
screen = pygame.display.set_mode((1000, 600))
clock = pygame.time.Clock()

# --------------------------------------- backgrounds ---------------------------------------
home_screen0 = pygame.transform.scale((pygame.image.load('assets/screen0.JPG')), (1000, 600))
home_screen1 = pygame.transform.scale((pygame.image.load('assets/screen1.PNG')), (1000, 600))
home_screen2 = pygame.transform.scale((pygame.image.load('assets/screen2.PNG')), (1000, 600))
# -------------------------------------------------------------------------------------------

jake = Jake()

# --------- changes screen ---------
screen_number = 1
def get_screen():
    global screen_number
    screens = {
        0: home_screen0,
        1: home_screen1,
        2: home_screen2
    }
    return screens[screen_number]
# ----------------------------------

# ------- for screen 0 -------
imposter_img = pygame.transform.scale((pygame.image.load('assets/imposter.png')), (64, 90))
imposter_group = pygame.sprite.Group()

class Imposter(pygame.sprite.Sprite):
    def __init__(self, group):
        pygame.sprite.Sprite.__init__(self)
        self.x = randint(20, 900)
        self.y = randint(20, 500)
        self.location = [self.x, self.y]

        self.image = imposter_img
        self.rect = self.image.get_rect()
        self.rect.center = self.location
        group.add(self)

    def update(self):
        move_x = randint(-10, 10)
        move_y = randint(-10, 10)
        rotate_amount = 10
        self.x += move_x
        self.y += move_y
        self.location = [self.x, self.y]

        self.image = pygame.transform.rotate(imposter_img, rotate_amount)
        self.rect = self.image.get_rect()
        self.rect.center = self.location
        rotate_amount += 10

imposter1 = Imposter(imposter_group)
imposter2 = Imposter(imposter_group)
imposter3 = Imposter(imposter_group)
imposter4 = Imposter(imposter_group)
imposter5 = Imposter(imposter_group)

# ----------------------------

index = 0
previous_time = 0

# ------------------ GAME LOOP ------------------
while running:
    previous_screen = screen_number

    # --------- limits animation framerate ---------
    if pygame.time.get_ticks()-previous_time > 150:
        index = (index + 1) % len(jake.jake_ss)
        previous_time = pygame.time.get_ticks()
    # ----------------------------------------------

    # --------- more movement stuffs ---------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                jake.moving_right = True
            if event.key == pygame.K_LEFT:
                jake.moving_left = True
            if event.key == pygame.K_UP:
                jake.moving_up = True
            if event.key == pygame.K_DOWN:
                pass

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                jake.moving_right = False
            if event.key == pygame.K_LEFT:
                jake.moving_left = False
            if event.key == pygame.K_UP:
                jake.moving_up = False
                jake.airborne = False
                jake.move_y = 20
            if event.key == pygame.K_DOWN:
                jake.moving_down = False

    jake.movement() # updates position on screen
    # ----------------------------------------

    # -------------- changes screen --------------
    if jake.location[0] < -20:
        if (not screen_number == 0):
            screen_number -=1
            jake.location[0] = screen.get_width()
        else:
            jake.location[0] = -20
    elif jake.location[0] > 1000:
        if (not screen_number == 2):
            screen_number += 1
            jake.location[0] = 0
        else:
            jake.location[0] = 1000
    # --------------------------------------------

    screen.blit(get_screen(), (0, 0))
    screen.blit(jake.jake_ss[index], (jake.location))

    current_screen = screen_number
    if (not current_screen == previous_screen):
        screening(screen_number)

    # --------- what have i made ---------
    if current_screen == 0:
        imposter_group.update()
        imposter_group.draw(screen)
    # ------------------------------------

    clock.tick(60) # 60 fps
    pygame.display.update()