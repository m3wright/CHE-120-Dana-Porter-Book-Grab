# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 20:28:05 2024

@author: Marcus
"""

import pygame , sys
from pygame import *
from sys import exit
from random import randint

ground_y=0
ground_x=0
pygame.init()
screen = pygame.display.set_mode((1200,800))
clock = pygame.time.Clock()
ground = pygame.image.load("floor 10.png").convert_alpha()
ground=pygame.transform.scale(ground, (2700,2700))
ground_rect = ground.get_rect(center=(400,200))

obstacle = pygame.image.load("cat_img.webp").convert_alpha()
obstacle = pygame.transform.scale(obstacle, (125,125))
obstacle_rect= obstacle.get_rect(center= (600,200))

player = pygame.image.load("fly_img.png").convert_alpha()
player = pygame.transform.scale(player, (75,75))
player_rect = player.get_rect(center= (600,400))


obstacle2_rect= obstacle.get_rect(center= (-600,200))

moveSpeed = 4

while True:
    screen.fill("White")
    mouse_pos = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a: 
                moveLeft = True
                ground_x=moveSpeed
            elif event.key == pygame.K_d:
                moveRight = True
                ground_x=-moveSpeed
            elif event.key == pygame.K_w: 
                moveUp=True
                ground_y=moveSpeed
            elif event.key == pygame.K_s: 
                moveDown=True
                ground_y=-moveSpeed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a: 
                moveLeft = True
                ground_x=0
            elif event.key == pygame.K_d:
                moveRight = True
                ground_x=0
            elif event.key == pygame.K_w: 
                moveUp=True
                ground_y=0
            elif event.key == pygame.K_s: 
                moveDown=True
                ground_y=0
                
    ground_rect.y += ground_y
    ground_rect.x += ground_x
    obstacle_rect.y += ground_y
    obstacle_rect.x += ground_x
    obstacle2_rect.y+=ground_y
    obstacle2_rect.x+= ground_x
    
    if player_rect.colliderect(obstacle_rect) or player_rect.colliderect(obstacle2_rect):
        if ground_x <0:
            ground_rect.x +=moveSpeed
            obstacle_rect.x +=moveSpeed
            obstacle2_rect.x+=moveSpeed
        elif ground_x > 0:
            ground_rect.x -=moveSpeed
            obstacle_rect.x -=moveSpeed
            obstacle2_rect.x -=moveSpeed
        
        if ground_y <0:
            ground_rect.y +=moveSpeed
            obstacle_rect.y +=moveSpeed
            obstacle2_rect.y +=moveSpeed
        elif ground_y > 0:
            ground_rect.y -=moveSpeed
            obstacle_rect.y -=moveSpeed
            obstacle2_rect.y -=moveSpeed
            
        #ground_x=0
        #ground_y=-2
            
    screen.blit(ground,ground_rect)
    
    screen.blit(obstacle,obstacle2_rect)
    screen.blit(obstacle,obstacle_rect)
    screen.blit(player,player_rect)
    
    #ground_y=0
    #ground_x=0
    
    pygame.display.update()
    clock.tick(60)