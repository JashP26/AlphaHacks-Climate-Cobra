import pygame as pg
from Settings_CC import *
import random

class Player(pg.sprite.Sprite):
    def __init__(self, img):
        pg.sprite.Sprite.__init__(self)
        self.image = img
        self.image.set_colorkey(WHITE)
        #self.image.fill(PURPLE)
        self.rect = self.image.get_rect()
        self.rect.center = (GAME_WIDTH / 2, GAME_HEIGHT / 2 )
        self.current_number = 0
        self.current_dir = "r"
        self.current_action = self.move_right()
        self.score = 0

    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_RIGHT]:
            self.proposed_number = 1
            if self.proposed_number  != self.current_number:
                self.current_action = self.move_right()
                self.current_number = self.proposed_number
        if keys[pg.K_UP]:
            self.proposed_number = 2
            if self.proposed_number != self.current_number:
                self.current_action = self.move_up()
                self.current_number = self.proposed_number
        if keys[pg.K_LEFT]:
            self.proposed_number = 1
            if self.proposed_number != self.current_number:
                self.current_action = self.move_left()
                self.current_number = self.proposed_number
        if keys[pg.K_DOWN]:
            self.proposed_number = 2
            if self.proposed_number != self.current_number:
                self.current_action = self.move_down()
                self.current_number = self.proposed_number

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.right > WIDTH - 300:
            self.rect.left = 0
        if self.rect.left < 0:
            self.rect.right = WIDTH - 300
        if self.rect.top < 0:
            self.rect.bottom = HEIGHT
        if self.rect.bottom > HEIGHT:
            self.rect.top = 0

    def move_right(self):
        self.speed_x = 3
        self.speed_y = 0
        self.propesed_number = 1

    def move_up(self):
        self.speed_x = 0
        self.speed_y = -3
        self.proposed_number = 2

    def move_left(self):
        self.speed_x = -3
        self.speed_y = 0
        self.proposed_number = 1

    def move_down(self):
        self.speed_x = 0
        self.speed_y = 3
        self.proposed_number = 2

class Collectables(pg.sprite.Sprite):
    def __init__(self, img):
        pg.sprite.Sprite.__init__(self)
        self.image = img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (COORDINATES[random.randrange(-1, 12)], COORDINATES[random.randrange(-1, 12)])
        self.check_coords()
        self.last_turn = pg.time.get_ticks()

    def check_coords(self):
        if self.rect.center in USED_COORDS:
            self.rect.center = (COORDINATES[random.randrange(-1, 12)], COORDINATES[random.randrange(-1, 12)])
            self.check_coords()
        else:
            USED_COORDS.append(self.rect.center)

class Pollution(pg.sprite.Sprite):
    def __init__(self, img):
        pg.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.center = (COORDINATES[random.randrange(-1, 12)], COORDINATES[random.randrange(-1, 12)])
        self.check_coords()

    def check_coords(self):
        if self.rect.center in USED_COORDS:
            self.rect.center = (COORDINATES[random.randrange(-1, 12)], COORDINATES[random.randrange(-1, 12)])
            self.check_coords()
        else:
            USED_COORDS.append(self.rect.center)

class Text_Box():
    def __init__(self, l, w, centerx, centery):
        self.image = pg.Surface((l, w))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (centerx, centery)