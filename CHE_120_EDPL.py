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
controlStart = None
floor1Start = None
floor2Start = None
floor3Start = None
floor4Start = None
floor5Start = None
floor6Start = None
floor7Start = None
floor8Start = None
floor9Start = None
floor10Start = None
endCreditStart = None

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
    
def floor1():
    pass

def floor2():
    pass

def floor3():
    pass

def floor4():
    pass

def floor5():
    pass

def floor6():
    pass

def floor7():
    pass

def floor8():
    pass

def floor9():
    pass

def floor10():
    pass

def endAnimation ():
    pass

def endCredits ():
    pass

while True:
    
    display.fill(WHITE)
    
    if introStart == None:
        introStart = intro()
        controlStart=True
        
    elif controlStart == True:
        floor1Start = control()
        
    elif floor1Start == True:
        floor2Start = floor1()
    
    elif floor2Start == True:
        floor3Start = floor2()
        
    elif floor3Start == True:
        floor4Start = floor3()
    
    elif floor4Start == True:
        floor5Start = floor4()
    
    elif floor5Start == True:
        floor6Start = floor5()
        
    elif floor6Start == True:
        floor7Start = floor6()
        
    elif floor7Start == True:
        floor8Start = floor7()
        
    elif floor8Start == True:
        floor9Start = floor8()
        
    elif floor9Start == True:
        floor10Start = floor9()
        
    elif floor10Start == True:
        endCreditStart = contro10()
    
    elif endCreditStart == True:
        pass
    
        
        
    
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS) 
