import pygame , sys
from pygame import *
from sys import exit
from random import randint
import random

ground_y=0
ground_x=0
blue_book_y = 0
blue_book_x = 0
pygame.init()
screen = pygame.display.set_mode((1200,800))
clock = pygame.time.Clock()
tile_size = 90
player_pos = 1
moveSpeed = 20
score = 0
start_time = 0
timesPlayed = 0

collected_books = []

book_apperence1 = True
book_apperence2 = False
book_apperence3 = False
book_apperence4 = False
book_apperence5 = False
book_apperence6 = False
book_apperence7 = False


game_done = False

introStart = True
controlStart = None
floor1Start = None
how_to_play_start = None
startOver = False


ground = pygame.image.load("Floor Design 10 - 6.png").convert_alpha()
ground=pygame.transform.scale(ground, (52*tile_size,53*tile_size))
ground_rect = ground.get_rect(topleft = (-7*tile_size,-18*tile_size))

table_img = pygame.image.load('Table top.png')
grass_img = pygame.image.load('Bookmid Horizontal.png')

br = pygame.image.load('Bookend Right.png').convert_alpha()
bl =pygame.image.load('Bookend Left.png').convert_alpha()
bu = pygame.image.load('Bookend up.png').convert_alpha()
bd =pygame.image.load('Bookend Down.png').convert_alpha()
bv =pygame.image.load('Bookmid vertical.png').convert_alpha()
bh =pygame.image.load('Bookmid Horizontal.png').convert_alpha()

player_forward = pygame.image.load("Move Forward.png").convert_alpha()
player_forward = pygame.transform.scale(player_forward, (80,80))
player_rect = player_forward.get_rect(center= (600,400))
player_forward_rect = player_forward.get_rect(center= (600,400))

player_back = pygame.image.load("Move Back.png").convert_alpha()
player_back = pygame.transform.scale(player_back, (80,80))
player_back_rect = player_back.get_rect(center= (600,400))

player_left = pygame.image.load("Move Left.png").convert_alpha()
player_left = pygame.transform.scale(player_left, (80,80))
player_left_rect = player_left.get_rect(center= (600,400))

player_right = pygame.image.load("Move Right.png").convert_alpha()
player_right = pygame.transform.scale(player_right, (80,80))
player_right_rect = player_right.get_rect(center= (600,400))

chair = pygame.image.load("chair.png").convert_alpha()
chair_up = pygame.image.load("chair up.png").convert_alpha()
chair_left = pygame.image.load("chair left.png").convert_alpha()
chair_right = pygame.image.load("chair right.png").convert_alpha()
iwall = pygame.image.load("iwall.png").convert_alpha()
owall = pygame.image.load("owall.png").convert_alpha()
table = pygame.image.load("table.png").convert_alpha()

#Random Book Generator
blue_book = pygame.image.load('Blue Book.png')
blue_book = pygame.transform.scale(blue_book, (tile_size, tile_size))
orange_book = pygame.image.load('Orange Image.png')
orange_book = pygame.transform.scale(orange_book, (tile_size, tile_size))
green_book = pygame.image.load('Green Image.png')
green_book = pygame.transform.scale(green_book, (tile_size, tile_size))
magenta_book = pygame.image.load('Magenta Book.png')
magenta_book = pygame.transform.scale(magenta_book, (tile_size, tile_size))
teal_book = pygame.image.load('Teal Book.png')
teal_book = pygame.transform.scale(teal_book, (tile_size, tile_size))
red_book = pygame.image.load('Red Book.png')
red_book = pygame.transform.scale(red_book, (tile_size, tile_size))
purple_book = pygame.image.load('Purple Book.png')
purple_book = pygame.transform.scale(purple_book, (tile_size, tile_size))


def random_blue(blue_book):
    blue_book_rect1 = blue_book.get_rect(center = (-270,3060))
    blue_book_rect2 = blue_book.get_rect(center = (2000,3035))
    blue_book_rect3 = blue_book.get_rect(center = (3300,3050))
    blue_book_rect4 = blue_book.get_rect(center = (2450,540))
    blue_book_rect5 = blue_book.get_rect(center = (3300,-1530))
    blue_book_rect6 = blue_book.get_rect(center = (800,-1260))
    return random.choice([blue_book_rect1,blue_book_rect2,blue_book_rect3,blue_book_rect4,blue_book_rect5,blue_book_rect6,])
    
def random_orange(orange_book):
    orange_book_rect1 = orange_book.get_rect(center = (220, 1260))
    orange_book_rect2 = orange_book.get_rect(center = (-300, -1260))
    orange_book_rect3 = orange_book.get_rect(center = (1000, 900))
    orange_book_rect4 = orange_book.get_rect(center = (2800, -100))
    orange_book_rect5 = orange_book.get_rect(center = (500, 200))
    orange_book_rect6 = orange_book.get_rect(center = (1800, 1900))

    return random.choice([orange_book_rect1,orange_book_rect2,orange_book_rect3,orange_book_rect4,orange_book_rect5,orange_book_rect6,])

def random_green (green_book):
    green_book_rect1 = green_book.get_rect(center = (-270,3060))
    green_book_rect2 = green_book.get_rect(center = (2000,3035))
    green_book_rect3 = green_book.get_rect(center = (3300,3050))
    green_book_rect4 = green_book.get_rect(center = (2450,540))
    green_book_rect5 = green_book.get_rect(center = (3300,-1530))
    green_book_rect6 = green_book.get_rect(center = (800,-1260))
    
    return random.choice([green_book_rect1,green_book_rect2,green_book_rect3,green_book_rect4,green_book_rect5,green_book_rect6,])

def random_magenta(magenta_book):
    magenta_book_rect1 = magenta_book.get_rect(center = (-300,-1260))
    magenta_book_rect2 = magenta_book.get_rect(center = (1000,900))
    magenta_book_rect3 = magenta_book.get_rect(center = (2800,-100))
    magenta_book_rect4 = magenta_book.get_rect(center = (500,200))
    magenta_book_rect5 = magenta_book.get_rect(center = (1800,1900))
    magenta_book_rect6 = magenta_book.get_rect(center = (220,1260))
    
    return random.choice([magenta_book_rect1,magenta_book_rect2,magenta_book_rect3,magenta_book_rect4,magenta_book_rect5,magenta_book_rect6,])


def random_teal(teal_book):
    teal_book_rect1 = teal_book.get_rect(center = (-270,3060))
    teal_book_rect2 = teal_book.get_rect(center = (2000,3035))
    teal_book_rect3 = teal_book.get_rect(center = (3300,3050))
    teal_book_rect4 = teal_book.get_rect(center = (2450,540))
    teal_book_rect5 = teal_book.get_rect(center = (3300,-1530))
    teal_book_rect6 = teal_book.get_rect(center = (800,-1260))
    
    return random.choice([teal_book_rect1,teal_book_rect2,teal_book_rect3,teal_book_rect4,teal_book_rect5,teal_book_rect6,])

def random_red(red_book):
    red_book_rect1 = red_book.get_rect(center = (220,1260))
    red_book_rect2 = red_book.get_rect(center = (1800,1900))
    red_book_rect3 = red_book.get_rect(center = (500,200))
    red_book_rect4 = red_book.get_rect(center = (2800,-100))
    red_book_rect5 = red_book.get_rect(center = (1000,900))
    red_book_rect6 = red_book.get_rect(center = (-300,-1260))
    
    return random.choice([red_book_rect1,red_book_rect2,red_book_rect3,red_book_rect4,red_book_rect5,red_book_rect6,])

def random_purple(purple_book):
    purple_book_rect1 = purple_book.get_rect(center = (800,-1260))
    purple_book_rect2 = purple_book.get_rect(center = (3300,-1530))
    purple_book_rect3 = purple_book.get_rect(center = (2450,540))
    purple_book_rect4 = purple_book.get_rect(center = (3300,3050))
    purple_book_rect5 = purple_book.get_rect(center = (2000,3035))
    purple_book_rect6 = purple_book.get_rect(center = (-270,3060))
    
    return random.choice([purple_book_rect1,purple_book_rect2,purple_book_rect3,purple_book_rect4,purple_book_rect5,purple_book_rect6,])

random_book1 = random_blue(blue_book)
random_book2 = random_orange(orange_book)
random_book3 = random_green(green_book)
random_book4 = random_magenta(magenta_book)
random_book5 = random_teal(teal_book)
random_book6 = random_red(red_book)
random_book7 = random_purple(purple_book)

fontObj2=pygame.font.Font('my_font.ttf', 60)
textSurfaceObj2 = fontObj2.render('Start Game', True, "Black", "White")
textRectObj2 = textSurfaceObj2.get_rect() 
textRectObj2.center = (600, 600)

fontObj1=pygame.font.Font('my_font.ttf', 80)
textSurfaceObj1 = fontObj1.render('Escape Dana Porter Library', True, "Black", "White") 
textRectObj1 = textSurfaceObj1.get_rect() 
textRectObj1.center = (600, 300)


Obj3_font = pygame.font.Font('my_font.ttf', 40)
Obj3_text_surface = Obj3_font.render('How to Play', True, 'Black', 'Grey')
Obj3_text_rect = Obj3_text_surface.get_rect(center = (600,100))

Obj4_font = pygame.font.Font('my_font.ttf', 40)
Obj4_text_surface = Obj4_font.render('Next', True, 'Black', 'Yellow')
Obj4_text_rect = Obj4_text_surface.get_rect(center = (1100,700))

instruction1 = 'Press the \"a\", \"s\", \"w\" and \"d\" keys to move.'
instruction2 = 'Collect all 7 books as fast as possible.'
instruction3 = 'To pick up a book, press the \"e\" key.'

Obj5_font = pygame.font.Font('my_font.ttf', 40)
Obj5_text_surface = Obj5_font.render(instruction1, True, 'Black', 'Grey')
Obj5_text_rect = Obj5_text_surface.get_rect(center = (600,300))
Obj6_font = pygame.font.Font('my_font.ttf', 40)
Obj6_text_surface = Obj6_font.render(instruction2, True, 'Black', 'Grey')
Obj6_text_rect = Obj6_text_surface.get_rect(center = (600,400))
Obj7_font = pygame.font.Font('my_font.ttf', 40)
Obj7_text_surface = Obj7_font.render(instruction3, True, 'Black', 'Grey')
Obj7_text_rect = Obj7_text_surface.get_rect(center = (600,500))

def intro ():
    screen.fill('White')
    screen.blit(textSurfaceObj1, textRectObj1) 
    screen.blit(textSurfaceObj2, textRectObj2) 
    
def how_to_play():
    screen.fill('Gray')
    screen.blit(Obj3_text_surface, Obj3_text_rect)
    screen.blit(Obj4_text_surface, Obj4_text_rect)
    screen.blit(Obj5_text_surface, Obj5_text_rect) 
    screen.blit(Obj6_text_surface, Obj6_text_rect)
    screen.blit(Obj7_text_surface, Obj7_text_rect)

def click_e():
    font = pygame.font.Font('my_font.ttf', 40)
    e_button = font.render('click E to pick up', False, (0,0,0))
    e_button_rect = e_button.get_rect(center = (400,400))
    screen.blit(e_button, e_button_rect)

def display_score():
    current_time = round((pygame.time.get_ticks()-start_time)/1000,1)
    score_surf = fontObj1.render(str(current_time), False , "Black")
    score_rect = score_surf.get_rect (topright = (1150,0))
    screen.blit(score_surf, score_rect)
    
    return current_time

def drawFlour10(ground_x, ground_y, moveSpeed):
    ground_rect.y += ground_y
    ground_rect.x += ground_x  
    
    random_book1.x += ground_x  
    random_book2.x += ground_x
    random_book3.x += ground_x
    random_book4.x += ground_x
    random_book5.x += ground_x
    random_book6.x += ground_x
    random_book7.x += ground_x
    
    random_book1.y += ground_y
    random_book2.y += ground_y
    random_book3.y += ground_y
    random_book4.y += ground_y
    random_book5.y += ground_y
    random_book6.y += ground_y
    random_book7.y += ground_y
    
    for tile in tile_list:
        tile[1].x += ground_x
        tile[1].y += ground_y
        
        pygame.draw.rect(screen, (255, 255, 255), tile[1], 2)
    
    for tile in tile_list:
        #check for collision in x direction
        if player_rect.colliderect(tile[1]):
            
            if ground_x < 0:
                ground_rect.x += moveSpeed
                random_book1.x += moveSpeed
                random_book2.x += moveSpeed
                random_book3.x += moveSpeed
                random_book4.x += moveSpeed
                random_book5.x += moveSpeed
                random_book6.x += moveSpeed
                random_book7.x += moveSpeed
                
            
            elif ground_x > 0:
                ground_rect.x -= moveSpeed
                random_book1.x -= moveSpeed
                random_book2.x -= moveSpeed
                random_book3.x -= moveSpeed
                random_book4.x -= moveSpeed
                random_book5.x -= moveSpeed
                random_book6.x -= moveSpeed
                random_book7.x -= moveSpeed
            
            if ground_y < 0:
                ground_rect.y += moveSpeed
                random_book1.y += moveSpeed
                random_book2.y += moveSpeed
                random_book3.y += moveSpeed
                random_book4.y += moveSpeed
                random_book5.y += moveSpeed
                random_book6.y += moveSpeed
                random_book7.y += moveSpeed
            
            elif ground_y > 0:
                ground_rect.y -= moveSpeed
                random_book1.y -= moveSpeed
                random_book2.y -= moveSpeed
                random_book3.y -= moveSpeed
                random_book4.y -= moveSpeed
                random_book5.y -= moveSpeed
                random_book6.y -= moveSpeed
                random_book7.y -= moveSpeed
            
            
            for tile in tile_list:
                if ground_x < 0:
                    tile[1].x += moveSpeed
                
                elif ground_x > 0:
                    tile[1].x -= moveSpeed
                
                if ground_y < 0:
                    tile[1].y += moveSpeed
                
                elif ground_y > 0:
                    tile[1].y -= moveSpeed 
    
    screen.blit(ground,ground_rect)
    
    for tile in tile_list:
        screen.blit(tile[0],tile[1])
    
    
def movePlayer(player_pos, ground_x, ground_y):
      
    if ground_x < 0:
        screen.blit(player_right,player_left_rect)
        player_pos = 1
    
    elif ground_x > 0:
        screen.blit(player_left,player_right_rect)
        player_pos = 2
        
    elif ground_y < 0:
        screen.blit(player_back,player_back_rect) 
        player_pos = 3
    
    elif ground_y > 0:
        screen.blit(player_forward,player_forward_rect)
        player_pos = 4
    
    else:
        if player_pos == 1:
            screen.blit(player_right,player_right_rect)
        
        elif player_pos == 2:
            screen.blit(player_left,player_left_rect)
        
        elif player_pos == 3:
            screen.blit(player_back,player_back_rect)
        
        elif player_pos == 4:
            screen.blit(player_forward,player_forward_rect)
    
    return player_pos

def blueBook():
    if book_apperence1:
        screen.blit(blue_book, random_book1)
        if player_rect.colliderect(random_book1) and timesPlayed == 0:
            click_e()
        
def orangeBook():
    if book_apperence2:
        screen.blit(orange_book, random_book2)

def greenBook():
    if book_apperence3:
        screen.blit(green_book, random_book3)

def magentaBook():
    if book_apperence4:
        screen.blit(magenta_book, random_book4)
        
def tealBook():
    if book_apperence5:
        screen.blit(teal_book, random_book5)
        
def redBook():
    if book_apperence6:
        screen.blit(red_book, random_book6)

def purpleBook():
    if book_apperence7: 
        screen.blit(purple_book, random_book7)
        
def showBooks(collected_books):
    for i in range(len(collected_books)):
        collected_books[i][1].x = i* tile_size
        collected_books[i][1].y = 0
        screen.blit(collected_books[i][0],collected_books[i][1])

world_data = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 0,10,14,14,11, 0,10,14,14,11, 0,10,14,14,11, 0,10,14,14,11, 0,10,14,14,11, 0,10,14,14,11, 0,10,14,14,11, 0,10,14,14,11, 0,10,14,14,11, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0,14,14, 0, 0, 0,14,14, 0, 0, 0,14,14, 0, 0, 0,14,14, 0, 0, 0,14,14, 0, 0, 0,14,14, 0, 0, 0,14,14, 0, 0, 0,14,14, 0, 0, 0,14,14, 0, 0, 0, 0, 0, 1],
[1, 8, 0, 8, 0,10,14,14,11, 0,10,14,14,11, 0,10,14,14,11, 0,10,14,14,11, 0,10,14,14,11, 0,10,14,14,11, 0,10,14,14,11, 0,10,14,14,11, 0,10,14,14,11, 0, 8, 0, 8, 1],
[1,14,14,14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,14,14,14, 1],
[1,14,14,14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,14,14,14, 1],
[1, 9, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 9, 1],
[1, 0, 0, 0, 0, 0, 0, 3, 7, 7, 7, 7, 7, 7, 7, 7, 7, 2, 0, 0,12,12,12,12,12,12,12,12,12,12,12,12,12,12, 0, 0, 3, 7, 7, 7, 7, 7, 7, 7, 7, 7, 2, 0, 0, 0, 0, 0, 0, 1],
[1, 8, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,12,13,13,13,13,13,13,13,13,13,13,13,13,12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 8, 1],
[1,14,14,14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,12,13,13,13,13,13,13,13,13,13,13,13,13,12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,14,14,14, 1],
[1,14,14,14, 0, 0, 0, 3, 7, 7, 7, 7, 7, 7, 7, 7, 7, 2, 0, 0,12,13,13,13,13,13,13,13,13,13,13,13,13,12, 0, 0, 3, 7, 7, 7, 7, 7, 7, 7, 7, 7, 2, 0, 0, 0,14,14,14, 1],
[1, 9, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,12,13,13,13,13,13,13,13,13,13,13,13,13,12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,12,13,13,13,13,13,13,13,13,13,13,13,13,12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 8, 0, 8, 0, 0, 0, 3, 7, 7, 7, 7, 7, 7, 7, 7, 7, 2, 0, 0,12,13,13,13,13,13,13,13,13,13,13,13,13,12, 0, 0, 3, 7, 7, 7, 7, 7, 7, 7, 7, 7, 2, 0, 0, 0, 8, 0, 8, 1],
[1,14,14,14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,12,13,13,13,13,13,13,13,13,13,13,13,13,12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,14,14,14, 1],
[1,14,14,14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,12,13,13,13,13,13,13,13,13,13,13,13,13,12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,14,14,14, 1],
[1, 9, 0, 9, 0, 0, 0, 3, 7, 7, 7, 7, 7, 7, 7, 7, 7, 2, 0, 0,12,13,13,13,13,13,13,13,13,13,13,13,13,12, 0, 0, 3, 7, 7, 7, 7, 7, 7, 7, 7, 7, 2, 0, 0, 0, 9, 0, 9, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,12,13,13,13,13,13,13,13,13,13,13,13,13,12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 8, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,12,12,12,12,12,12,13,13,13,13,13,13,13,12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 8, 1],
[1,14,14,14, 0, 0, 0, 3, 7, 7, 7, 7, 7, 7, 7, 7, 7, 2, 0, 0, 0, 0, 0, 0, 0,12,12,12,12,12,12,12,12,12, 0, 0, 3, 7, 7, 7, 7, 7, 7, 7, 7, 7, 2, 0, 0, 0,14,14,14, 1],
[1,14,14,14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,14,14,14, 1],
[1, 9, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,12,12,12,12,12,12,12,12,12, 0, 0, 0, 9, 0, 9, 1],
[1, 0, 0, 0, 0, 0, 0,12,12,12,12,12,12,12, 0, 0, 0, 0, 0, 0, 0, 3, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 2, 0, 0, 0, 0,12,13,13,13,13,13,13,13,12, 0, 0, 0, 0, 0, 0, 1],
[1, 8, 0, 8, 0, 0, 0,12,13,13,13,13,13,12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,12,13,13,13,13,13,13,13,12, 0, 0, 0, 8, 0, 8, 1],
[1,14,14,14, 0, 0, 0,12,13,13,13,13,13,12,12,12,12,12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,12,13,13,13,13,13,13,13,12, 0, 0, 0,14,14,14, 1],
[1,14,14,14, 0, 0, 0,12,13,13,13,13,13,13,13,13,13,12, 0, 0, 0, 3, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 2, 0, 0, 0, 0,12,13,13,13,13,13,13,13,12, 0, 0, 0,14,14,14, 1],
[1, 9, 0, 9, 0, 0, 0,12,13,13,13,13,13,13,13,13,13,12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,12,12,12,13,13,13,13,13,13,13,12, 0, 0, 0, 9, 0, 9, 1],
[1, 0, 0, 0, 0, 0, 0,12,13,13,13,13,13,13,13,13,13,12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,12,13,13,13,13,13,13,13,13,13,12, 0, 0, 0, 0, 0, 0, 1],
[1, 8, 0, 8, 0, 0, 0,12,13,13,13,13,13,13,13,13,13,12, 0, 0, 0, 3, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 2, 0, 0,12,13,13,13,13,13,13,13,13,13,12, 0, 0, 0, 8, 0, 8, 1],
[1,14,14,14, 0, 0, 0,12,13,13,13,13,13,13,13,13,13,12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,12,13,13,13,13,13,13,13,13,13,12, 0, 0, 0,14,14,14, 1],
[1,14,14,14, 0, 0, 0,12,13,13,13,13,13,13,13,13,13,12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,12,13,13,13,13,13,13,13,13,13,12, 0, 0, 0,14,14,14, 1],
[1, 9, 0, 9, 0, 0, 0,12,12,12,12,12,12,12,12,12,12,12, 0, 0, 0, 3, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 2, 0, 0,12,12,12,12,12,12,12,12,12,12,12, 0, 0, 0, 9, 0, 9, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 8, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 8, 1],
[1,14,14,14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,14,14,14, 1],
[1,14,14,14, 0, 0, 0, 3, 7, 7, 7, 7, 7, 7, 7, 7, 7, 2, 0, 0, 0, 3, 7, 7, 7, 7, 7, 7, 7, 7, 7, 2, 0, 0, 0, 0, 3, 7, 7, 7, 7, 7, 7, 7, 7, 7, 2, 0, 0, 0,14,14,14, 1],
[1, 9, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 8, 0, 8, 0, 0, 0, 3, 7, 7, 7, 7, 7, 7, 7, 7, 7, 2, 0, 0, 0, 3, 7, 7, 7, 7, 7, 7, 7, 7, 7, 2, 0, 0, 0, 0, 3, 7, 7, 7, 7, 7, 7, 7, 7, 7, 2, 0, 0, 0, 8, 0, 8, 1],
[1,14,14,14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,14,14,14, 1],
[1,14,14,14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,14,14,14, 1],
[1, 9, 0, 9, 0, 0, 0, 3, 7, 7, 7, 7, 7, 7, 7, 7, 7, 2, 0, 0, 0, 3, 7, 7, 7, 7, 7, 7, 7, 7, 7, 2, 0, 0, 0, 0, 3, 7, 7, 7, 7, 7, 7, 7, 7, 7, 2, 0, 0, 0, 9, 0, 9, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 8, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 8, 1],
[1,14,14,14, 0, 0, 0, 3, 7, 7, 7, 7, 7, 7, 7, 7, 7, 2, 0, 0, 0, 3, 7, 7, 7, 7, 7, 7, 7, 7, 7, 2, 0, 0, 0, 0, 3, 7, 7, 7, 7, 7, 7, 7, 7, 7, 2, 0, 0, 0,14,14,14, 1],
[1,14,14,14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,14,14,14, 1],
[1, 9, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 9, 1],
[1, 0, 0, 0, 0, 0, 0, 3, 7, 7, 7, 7, 7, 7, 7, 7, 7, 2, 0, 0, 0, 3, 7, 7, 7, 7, 7, 7, 7, 7, 7, 2, 0, 0, 0, 0, 3, 7, 7, 7, 7, 7, 7, 7, 7, 7, 2, 0, 0, 0, 0, 0, 0, 1],
[1, 8, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 8, 1],
[1,14,14,14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,14,14,14, 1],
[1,14,14,14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,14,14,14, 1],
[1, 9, 0, 9, 0,10,14,14,11, 0,10,14,14,11, 0,10,14,14,11, 0,10,14,14,11, 0,10,14,14,11, 0,10,14,14,11, 0,10,14,14,11, 0,10,14,14,11, 0,10,14,14,11, 0, 9, 0, 9, 1],
[1, 0, 0, 0, 0, 0,14,14, 0, 0, 0,14,14, 0, 0, 0,14,14, 0, 0, 0,14,14, 0, 0, 0,14,14, 0, 0, 0,14,14, 0, 0, 0,14,14, 0, 0, 0,14,14, 0, 0, 0,14,14, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0,10,14,14,11, 0,10,14,14,11, 0,10,14,14,11, 0,10,14,14,11, 0,10,14,14,11, 0,10,14,14,11, 0,10,14,14,11, 0,10,14,14,11, 0,10,14,14,11, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],

]

tile_list = []


 
def init_map():
    row_count =-19
    for row in world_data:
        col_count = -7 
        for tile in row:
            if tile == 1:
                img = pygame.transform.scale(table_img, (tile_size, tile_size))
                img_rect = img.get_rect(topright = (col_count*tile_size,row_count*tile_size))
                tile = (img, img_rect)
                tile_list.append(tile)
            elif tile == 2:
                img = pygame.transform.scale(br, (tile_size, tile_size))
                img_rect = img.get_rect(topright = (col_count*tile_size,row_count*tile_size))
                tile = (img, img_rect)
                tile_list.append(tile)
                
            elif tile == 3:
                img = pygame.transform.scale(bl, (tile_size, tile_size))
                img_rect = img.get_rect(topright = (col_count*tile_size,row_count*tile_size))
                tile = (img, img_rect)
                tile_list.append(tile)
            
            elif tile == 4:
                img = pygame.transform.scale(bu, (tile_size, tile_size))
                img_rect = img.get_rect(topright = (col_count*tile_size,row_count*tile_size))
                tile = (img, img_rect)
                tile_list.append(tile)
                    
            elif tile == 5:
                img = pygame.transform.scale(bd, (tile_size, tile_size))
                img_rect = img.get_rect(topright = (col_count*tile_size,row_count*tile_size))
                tile = (img, img_rect)
                tile_list.append(tile)
                
            elif tile == 6:
                img = pygame.transform.scale(bv, (tile_size, tile_size))
                img_rect = img.get_rect(topright = (col_count*tile_size,row_count*tile_size))
                tile = (img, img_rect)
                tile_list.append(tile)
            
            elif tile == 7:
                img = pygame.transform.scale(bh, (tile_size, tile_size))
                img_rect = img.get_rect(topright = (col_count*tile_size,row_count*tile_size))
                tile = (img, img_rect)
                tile_list.append(tile)
                
            elif tile == 8:
                img = pygame.transform.scale(chair, (tile_size, tile_size))
                img_rect = img.get_rect(topright = (col_count*tile_size,row_count*tile_size))
                tile = (img, img_rect)
                tile_list.append(tile)
            
            elif tile == 9:
                img = pygame.transform.scale(chair_up, (tile_size, tile_size))
                img_rect = img.get_rect(topright = (col_count*tile_size,row_count*tile_size))
                tile = (img, img_rect)
                tile_list.append(tile)
            
            elif tile == 10:
                img = pygame.transform.scale(chair_left, (tile_size, tile_size))
                img_rect = img.get_rect(topright = (col_count*tile_size,row_count*tile_size))
                tile = (img, img_rect)
                tile_list.append(tile)
            
            elif tile == 11:
                img = pygame.transform.scale(chair_right, (tile_size, tile_size))
                img_rect = img.get_rect(topright = (col_count*tile_size,row_count*tile_size))
                tile = (img, img_rect)
                tile_list.append(tile)
            
            elif tile == 12:
                img = pygame.transform.scale(owall, (tile_size, tile_size))
                img_rect = img.get_rect(topright = (col_count*tile_size,row_count*tile_size))
                tile = (img, img_rect)
                tile_list.append(tile)
                
            elif tile == 13:
                img = pygame.transform.scale(iwall, (tile_size, tile_size))
                img_rect = img.get_rect(topright = (col_count*tile_size,row_count*tile_size))
                tile = (img, img_rect)
                tile_list.append(tile)
            
            elif tile == 14:
                img = pygame.transform.scale(table, (tile_size, tile_size))
                img_rect = img.get_rect(topright = (col_count*tile_size,row_count*tile_size))
                tile = (img, img_rect)
                tile_list.append(tile)
        
            col_count += 1
        row_count += 1
    row_count = 0
    col_count = 0

textSurfaceObj3 = fontObj1.render('You Won!', True, "Black", "White") 
textRectObj3 = textSurfaceObj3.get_rect() 
textRectObj3.center = (600, 150)

textSurfaceObj4 = fontObj1.render('Would You Like to Play Again?', True, "Black", "White") 
textRectObj4 = textSurfaceObj4.get_rect() 
textRectObj4.center = (600, 300)

textSurfaceObj5 = fontObj1.render('Yes', True, "Black", "White") 
textRectObj5 = textSurfaceObj5.get_rect() 
textRectObj5.center = (300, 600)

textSurfaceObj6 = fontObj1.render('No', True, "Black", "White") 
textRectObj6 = textSurfaceObj6.get_rect() 
textRectObj6.center = (900, 600)




def game_won():
    screen.fill('White')
    screen.blit(textSurfaceObj3,textRectObj3)
    screen.blit(textSurfaceObj4,textRectObj4)
    screen.blit(textSurfaceObj5,textRectObj5)
    screen.blit(textSurfaceObj6,textRectObj6)
    

init_map()

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a: 
                
                ground_x=moveSpeed
                
            elif event.key == pygame.K_d:
                
                ground_x=-moveSpeed
                
            elif event.key == pygame.K_w: 
                
                ground_y=moveSpeed
                blue_book_y = moveSpeed
            elif event.key == pygame.K_s: 
                moveDown=True
                ground_y=-moveSpeed
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                
                ground_x=0
                
            elif event.key == pygame.K_d:
                
                ground_x=0
                
            elif event.key == pygame.K_w: 
                
                ground_y=0
                
            elif event.key == pygame.K_s: 
                ground_y=0
        
        if player_rect.colliderect(random_book1):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    book_apperence1 = False
                    book_apperence2 = True
                    collected_books.append([blue_book,random_book1])
                    
        elif player_rect.colliderect(random_book2) and book_apperence2:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    book_apperence2 = False
                    book_apperence3 = True
                    collected_books.append([orange_book,random_book2])
                    
        elif player_rect.colliderect(random_book3) and book_apperence3:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    book_apperence3 = False
                    book_apperence4 = True
                    collected_books.append([green_book,random_book3])
        
        elif player_rect.colliderect(random_book4)and book_apperence4:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    book_apperence4 = False
                    book_apperence5 = True
                    collected_books.append([magenta_book,random_book4])
                    
        elif player_rect.colliderect(random_book5)and book_apperence5:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    book_apperence5 = False
                    book_apperence6 = True
                    collected_books.append([teal_book,random_book5])
        
        elif player_rect.colliderect(random_book6)and book_apperence6:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    book_apperence6 = False
                    book_apperence7 = True
                    collected_books.append([red_book,random_book6])
                    
        elif player_rect.colliderect(random_book7)and book_apperence7:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    book_apperence7 = False
                    game_done = True
                    collected_books.append([purple_book,random_book7])
                    
        if event.type == pygame.MOUSEBUTTONDOWN  :
            if textRectObj2.collidepoint(event.pos):
                how_to_play_start = True
                introStart = False
                
            elif textRectObj5.collidepoint(event.pos):
                startOver = True
                
            elif textRectObj6.collidepoint(event.pos):
                pygame.quit() 
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if Obj4_text_rect.collidepoint(event.pos):
                controlStart = True
                how_to_play_start = False
                start_time = pygame.time.get_ticks()
                
    if introStart:
        introStart = intro()
        
    elif how_to_play_start == True:
        how_to_play_start == how_to_play()
    
    
        
    elif controlStart:
        
        screen.fill("Grey")
        
        drawFlour10(ground_x, ground_y, moveSpeed)
        
        player_pos = movePlayer(player_pos, ground_x, ground_y)
        
        blueBook()
        
        orangeBook()
        
        greenBook()
        
        magentaBook()
        
        tealBook()
        
        redBook()
        
        purpleBook()
        
        showBooks(collected_books)
        
        score = display_score()
        
    elif how_to_play_start == True:
        how_to_play_start == how_to_play()
    
    if len(collected_books)==7:
        controlStart=False
        game_won()
        score_message = fontObj1.render(f'your score: {score}',False,"Green")
        score_message_rect = score_message.get_rect(center = (600,450)) 
        screen.blit(score_message,score_message_rect)
        
        if startOver:
            timesPlayed +=1
            start_time = pygame.time.get_ticks()
            ground_rect.x = -7*tile_size
            ground_rect.y = -18*tile_size
            tile_list.clear()
            init_map()
            controlStart = True
            book_apperence1 = True
            book_apperence2 = False
            book_apperence3 = False
            book_apperence4 = False
            book_apperence5 = False
            book_apperence6 = False
            book_apperence7 = False
            score = 0
            collected_books.clear()
            random_book1 = random_blue(blue_book)
            random_book2 = random_orange(orange_book)
            random_book3 = random_green(green_book)
            random_book4 = random_magenta(magenta_book)
            random_book5 = random_teal(teal_book)
            random_book6 = random_red(red_book)
            random_book7 = random_purple(purple_book)
            startOver = False
            
            

           
        
    #row_count = 0
    

    #ground_y=0
    #ground_x=0
    
    pygame.display.update()
    clock.tick(60)