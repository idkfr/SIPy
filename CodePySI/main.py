import pygame, sys
from joueur import Joueur
#test comment
class Game:
    def __init__(self):
        joueur_sprite = Joueur((screen_width / 2,screen_heigth),screen_width,screen_heigth,5)
        self.joueur = pygame.sprite.GroupSingle(joueur_sprite)

    def run(self):
        self.joueur.update()
        self.joueur.draw(screen)
        #update all sprite groups
        #draw all sprite groups
if __name__ == '__main__':
    pygame.init()
    screen_width = 600
    screen_heigth = 600
    screen = pygame.display.set_mode((screen_width,screen_heigth))
    clock = pygame.time.Clock()
    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
        screen.fill((30,30,30))
        game.run()

        pygame.display.flip()
        clock.tick(60)