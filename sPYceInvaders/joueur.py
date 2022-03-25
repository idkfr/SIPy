from tkinter import TRUE
import pygame
from pygame.locals import *

class Joueur(pygame.sprite.Sprite):
    def __init__(self,pos,constraint_x,constraint_y,speed):
        super().__init__()
        self.image = pygame.Surface([30, 30])
        self.image.fill('blue')
        self.rect = self.image.get_rect(midbottom = pos)
        self.speed = speed
        self.max_x_constraint = constraint_x
        self.max_y_constraint = constraint_y
        self.ready = True
        self.laser_time = 0
        self.laser_cooldown = 600



    def get_input(self):
        self.key_pressed = pygame.key.get_pressed()
        self.mouse_pressed = pygame.mouse.get_pressed()
        if self.key_pressed[K_d]:
            self.rect.x += self.speed
        if self.key_pressed[K_q]:
            self.rect.x -= self.speed
        if self.key_pressed[K_z]:
            self.rect.y -= self.speed
        if self.key_pressed[K_s]:
            self.rect.y += self.speed
        if self.mouse_pressed[0] and  self.ready:
            self.shoot_laser()
            self.ready = False
            self.laser_time = pygame.time.get_ticks()
            

    def recharge(self):
        if not self.ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_time >= self.laser_cooldown:
                self.ready = TRUE
        

    def constraint(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        elif self.rect.right >= self.max_x_constraint:
            self.rect.right = self.max_x_constraint
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= self.max_y_constraint:
            self.rect.bottom = self.max_y_constraint
        
    
    def shoot_laser(self):
        print('shoot laser')

    def update(self):
        self.get_input()
        self.constraint()
        self.recharge()
