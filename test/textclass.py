import pygame

class Text():
    def __init__(self):
        pygame.font.init()
        self.textX = 50
        self.textY = 50
        self.fontDir = None
        self.font = pygame.font.Font(self.fontDir, 32)
        
    def disp_text(self, ecran):
        self.textToPrint = 'a'
        self.textPrint = pygame.font.Font.render(self.font, self.textToPrint, False, 'red')
        ecran.blit(self.textPrint, (self.textX, self.textY))
        
