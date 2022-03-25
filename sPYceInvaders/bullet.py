import pygame



class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 1
        self.image = pygame.Surface([5, 15])
        
