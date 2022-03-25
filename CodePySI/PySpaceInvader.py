import pygame, math, random, time, sys
from textclass import Text
from meteorite import Meteorite
from joueur import Joueur
from pygame.math import Vector2
from pygame.locals import *

# test comment


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255,0,0)



class main:
    def __init__(self):
        self.DIMSCREEN = (1200, 800)
        self.ecran = pygame.display.set_mode(self.DIMSCREEN)
        self.x, self.y = self.ecran.get_size()

    def reglages(self):
        self.clock = pygame.time.Clock()
        self.clock.tick(60)
        pygame.display.set_caption('Shooter')
        self.ecran.fill(BLACK)
        
        self.timer = 0

    def get_timer(self, time):
        
        self.tick = self.clock.tick()
        self.timer += self.tick
        
        if self.timer >= time:
            self.timer = 0
            return True
        return False

    def start(self):
        self.reglages()
        
        
        self.meteorites = []
        self.meteoriteGroup = pygame.sprite.Group()
        self.joueurGroup = pygame.sprite.Group()
        self.joueurGroup.add(Joueur((self.DIMSCREEN[0] / 2, self.DIMSCREEN[1] / 2), self.DIMSCREEN[0], self.DIMSCREEN[1], 1))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                
            
            self.ecran.fill(BLACK)

            Text().disp_text(self.ecran)
  
            if self.get_timer(1000):
                self.meteoriteGroup.add(Meteorite(35, 35, 'red', self.DIMSCREEN[1]))
            
            self.meteoriteGroup.draw(self.ecran)
            self.meteoriteGroup.update()
            self.joueurGroup.draw(self.ecran)
            self.joueurGroup.update()
            


            pygame.display.update()




m = main()
m.start()





# import pygame, math, random, time
# from pygame.math import Vector2

# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# RED = (255,0,0)



# class Setup:
#     def __init__(self):

#         self.DIM_SCREEN = (1200, 800)
#         self.ecran = pygame.display.set_mode(self.DIM_SCREEN)
#         self.x, self.y = self.ecran.get_size()
    
#     def reglages(self):
#         self.clock = pygame.time.Clock()
#         self.clock.tick(60)
#         pygame.display.set_caption('Shooter')
#         self.ecran.fill(BLACK)




           
            
#             Text().dispText()
           
            
            
            


             
            
#             pygame.display.update()
            


        



        





# s = Setup()



# s.start()

