import pygame, sys
from pygame.locals import *
import time 

pygame.init()
#SET UP THE WINDOW

DISPLAYSURF = pygame.display.set_mode((1500,900),0,32)
pygame.display.set_caption('Drawing')

#set up the colours
BLACK = (0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)

#draw on the surface object
DISPLAYSURF.fill(WHITE)
pygame.draw.polygon(DISPLAYSURF,GREEN,((146,0),(291,106),(236,277),(56,277),(0,106)))
pygame.draw.line(DISPLAYSURF,BLUE,(60,60),(120,60),4)
pygame.draw.line(DISPLAYSURF,BLUE,(120,60),(60,120))
pygame.draw.line(DISPLAYSURF,BLUE,(60,120),(120,120))
pygame.draw.circle(DISPLAYSURF, RED,(300,50),20,0)
pygame.draw.ellipse(DISPLAYSURF,RED,(300,250,40,80),1)
pygame.draw.rect(DISPLAYSURF,RED,(200,150,100,50))

pixObj = pygame.PixelArray(DISPLAYSURF)
pixObj[480][380]=BLACK
pixObj[482][382] = BLACK 
pixObj[484][384] = BLACK 
pixObj[486][386] = BLACK
pixObj[488][388] = BLACK
del pixObj 

catImg = pygame.image.load('fox.jpg') 

catImg = pygame.transform.scale(catImg, (300, 180))
catx=10
caty=10

FPS = 30 
fpsClock = pygame.time.Clock()

direction = "right"

fontObj=pygame.font.Font('STIXGeneralBol.ttf', 100)
textSurfaceObj = fontObj.render('Hello world!', True, BLACK, WHITE) 
textRectObj = textSurfaceObj.get_rect() 
textRectObj.center = (800, 400)


soundObj = pygame.mixer.Sound('sound.mp3') 
#soundObj.play() 

#time.sleep(13)
soundObj.stop() 

pygame.mixer.music.load('sound.mp3')
pygame.mixer.music.play(-1, 0.0)

while True:
    
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj) 
    if direction == "right":
        catx+=5
        if catx==280:
            direction ='down'
    elif direction =='down':
        caty+=5
        if caty==220:
            direction = 'left'
    elif direction == "left":
        catx-=5
        if catx==10:
            direction ='up'
    elif direction == "up":
        caty-=5
        if caty==10:
            direction ='right'
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    DISPLAYSURF.blit(catImg, (catx, caty)) 
    
    pygame.display.update()
    fpsClock.tick(FPS) 
    