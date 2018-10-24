import sys
import pygame 
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("天道酬勤")
GOLD = 255,251,255
BLUE = 255,251,0

myfont = pygame.font.Font(None,60)
textImage = myfont.render("HELLO PYGAME",True,GOLD)
#f1 = pygame.freetype.Font("C://Windows//Font//msyh.ttc",36)
#f1rect = f1.render_to(screen,(200,160),"唐雪利",fgcolor = GOLD,size = 10)

while True :
	for event in pygame.event.get() :
		if event.type == pygame.QUIT :
			sys.exit()
	screen.fill(BLUE)
	screen.blit(textImage,(100,180))
	pygame.display.update()