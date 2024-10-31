# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 10:36:59 2024

@author: Marcus
"""


import pygame, sys
from pygame.locals import *
import time 

display = pygame.display.set_mode((1500,900),0,32)
pygame.display.set_caption('CHE 120 Project')

pygame.init()

FPS = 30 
fpsClock = pygame.time.Clock()

BLACK= (  0,  0,  0)
WHITE= (255,255,255)
RED=   (255,  0,  0)
GREEN= (0  ,255,  0)
BLUE=  (0  ,  0,255)


introStart = None

def intro ():
    fontObj=pygame.font.Font('STIXGeneralBol.ttf', 100)
    textSurfaceObj = fontObj.render('Escape Danna Porter Library', True, BLACK, WHITE) 
    textRectObj = textSurfaceObj.get_rect() 
    textRectObj.center = (800, 400)
    display.blit(textSurfaceObj, textRectObj) 
    
    
    startButton = False
    
    if startButton == True:
        return False
    
def controls ():
    pass

def Movement ():
    pass
    
def objectPickUp ():
    pass
    
def Floor1():
    pass

def Floor2():
    pass

def Floor3():
    pass

def Floor4():
    pass

def Floor5():
    pass

def Floor6():
    pass

def Floor7():
    pass

def Floor8():
    pass

def Floor9():
    pass

def Floor10():
    pass

while True:
    
    display.fill(WHITE)
    
    if introStart == None:
        introStart = intro()
        
    
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS) 
