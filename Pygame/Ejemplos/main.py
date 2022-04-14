import  pygame, sys
from pygame.locals import *

pygame.init()
DS = pygame.display.set_mode((800,600),0 , 32)
pygame.display.set_caption('Pantalla de inicio')
WHITE =(255,255,255)
RED =(255,0,0)


pygame.draw.line(DS, RED, (60,60), (120,60), 4)

DS.fill(WHITE)


pixObj = pygame.PixelArray(DS)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()