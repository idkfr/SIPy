from distutils.errors import DistutilsModuleError
import pygame, random


class Meteorite(pygame.sprite.Sprite):
    def __init__(self, width, height, color, dimY):
        super().__init__()
        self.posY = -30
        self.dimY = dimY
        self.randX = random.randint(30, 1170)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        
        

    def update(self):
        
        if self.posY > self.dimY:
            self.kill()
        self.rect.center = [self.randX, self.posY]
        self.posY += 0.3
