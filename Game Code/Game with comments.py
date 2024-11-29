#MW = Marcus Wright
#MS = Michael Small

#MW: Imports all the necessary modules
import pygame , sys
from pygame import *
from sys import exit
from random import randint
import random
            
#MW defines all the variables
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
tile_list = []

#MS - These are the random book appearance variables.
#When, during the game loop, the code determines that the player has picked up a book 
#the first one swiches to false and the next one switches to true. This continues until the game ends.
book_apperence1 = True
book_apperence2 = False
book_apperence3 = False
book_apperence4 = False
book_apperence5 = False
book_apperence6 = False
book_apperence7 = False

#MW game state variables
introStart = True
controlStart = None
floor1Start = None
how_to_play_start = None
startOver = False

#MW caption for game window
pygame.display.set_caption("Dana Porter Book Grab")

#MW imports all of the images and image rectangles for the game
#MW floor desiggn for the game
ground = pygame.image.load("Floor Design.png").convert_alpha()
ground=pygame.transform.scale(ground, (52*tile_size,53*tile_size))
ground_rect = ground.get_rect(topleft = (-7*tile_size,-18*tile_size))
#MW bookshelf tile images
table_img = pygame.image.load('Table top.png')
br = pygame.image.load('Bookend Right.png').convert_alpha()
bl =pygame.image.load('Bookend Left.png').convert_alpha()
bu = pygame.image.load('Bookend up.png').convert_alpha()
bd =pygame.image.load('Bookend Down.png').convert_alpha()
bv =pygame.image.load('Bookmid vertical.png').convert_alpha()
bh =pygame.image.load('Bookmid Horizontal.png').convert_alpha()
#MW player forward postion image and rectangle
player_forward = pygame.image.load("Move Forward.png").convert_alpha()
player_forward = pygame.transform.scale(player_forward, (70,70))
player_rect = player_forward.get_rect(center= (600,400))
player_forward_rect = player_forward.get_rect(center= (600,400))
#MW player back postion image and rectangle
player_back = pygame.image.load("Move Back.png").convert_alpha()
player_back = pygame.transform.scale(player_back, (70,70))
player_back_rect = player_back.get_rect(center= (600,400))
#MW player left postion image and rectangle
player_left = pygame.image.load("Move Left.png").convert_alpha()
player_left = pygame.transform.scale(player_left, (70,70))
player_left_rect = player_left.get_rect(center= (600,400))
#MW player right postion image and rectangle
player_right = pygame.image.load("Move Right.png").convert_alpha()
player_right = pygame.transform.scale(player_right, (70,70))
player_right_rect = player_right.get_rect(center= (600,400))
#MW micellaneous tiles
chair = pygame.image.load("chair.png").convert_alpha()
chair_up = pygame.image.load("chair up.png").convert_alpha()
chair_left = pygame.image.load("chair left.png").convert_alpha()
chair_right = pygame.image.load("chair right.png").convert_alpha()
iwall = pygame.image.load("iwall.png").convert_alpha()
owall = pygame.image.load("owall.png").convert_alpha()
table = pygame.image.load("table.png").convert_alpha()

#MS - Random Book Generator
#After initiallizing the book images, I scaled them up to the same size as the tiles.
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

#MS - Using the rectangle method, I set six different positions for each of the 7 books.
#Using the random module, each of these functions will choose one of the six different positions and place the book on the set coordinates.
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

#MS - These are the varables assigned to whatever book possitions the above functions choose.
#These will be called later in the game loop.
random_book1 = random_blue(blue_book)
random_book2 = random_orange(orange_book)
random_book3 = random_green(green_book)
random_book4 = random_magenta(magenta_book)
random_book5 = random_teal(teal_book)
random_book6 = random_red(red_book)
random_book7 = random_purple(purple_book)

#MW imports fonts and defines word objects and rectangles for each word object
fontObj2=pygame.font.Font('my_font.ttf', 60)
textSurfaceObj2 = fontObj2.render('Start Game', True, "Black", "White")
textRectObj2 = textSurfaceObj2.get_rect() 
textRectObj2.center = (600, 600)

fontObj1=pygame.font.Font('my_font.ttf', 80)
textSurfaceObj1 = fontObj1.render('Dana Porter Book Grab', True, "Black", "Grey") 
textRectObj1 = textSurfaceObj1.get_rect() 
textRectObj1.center = (600, 300)

#MS - These are the fonts and messages for the how to play screen.
#These fonts are converted to rectangles so they can be placed acurately on the screen.
Obj3_font = pygame.font.Font('my_font.ttf', 40)
Obj3_text_surface = Obj3_font.render('How to Play', True, 'Black', 'Grey')
Obj3_text_rect = Obj3_text_surface.get_rect(center = (600,100))

Obj4_font = pygame.font.Font('my_font.ttf', 40)
Obj4_text_surface = Obj4_font.render('Next', True, 'Black', 'Yellow')
Obj4_text_rect = Obj4_text_surface.get_rect(center = (1100,700))

#MS - These are the instructions for the how to play screen and will be blitted like the above messages.
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

#initializes all the game sound effects and the game music
pickUpSound = pygame.mixer.Sound('item-equip-6904.mp3') 
pygame.mixer.music.load('Distant-Sky-Epic-Hybrid-Music-chosic.com_.mp3')
#plays the game music in a infinite loop
pygame.mixer.music.play(-1, 0.0)



#MW function that blits the intro screen
def intro ():
    #MW fills screen and blits two text objects
    screen.fill('Gray')
    screen.blit(textSurfaceObj1, textRectObj1) 
    screen.blit(textSurfaceObj2, textRectObj2) 

#MS - This is the function that blits all the how to play fonts and messages onto the screen.
def how_to_play():
    screen.fill('Gray')
    screen.blit(Obj3_text_surface, Obj3_text_rect)
    screen.blit(Obj4_text_surface, Obj4_text_rect)
    screen.blit(Obj5_text_surface, Obj5_text_rect) 
    screen.blit(Obj6_text_surface, Obj6_text_rect)
    screen.blit(Obj7_text_surface, Obj7_text_rect)

#MS - This is the function that, when called, remindes the player to click e to pick up a book.
def click_e():
    font = pygame.font.Font('my_font.ttf', 40)
    e_button = font.render('click E to pick up', False, (0,0,0))
    e_button_rect = e_button.get_rect(center = (400,400))
    screen.blit(e_button, e_button_rect)

#MW displays a timer on the screen while the game is running 
def display_score():
    #MW calculates the time the level attempt started by substracting the total time by the time at which the start button was pressed
    #MW is them devided by 1000 to get seconds from miliseconds and it is rounded to two decimal places
    current_time = round((pygame.time.get_ticks()-start_time)/1000,1)
    #MW defines text objects for the score value and blits it onto the screen
    score_surf = fontObj1.render(str(current_time), False , "Black")
    score_rect = score_surf.get_rect (topright = (1150,0))
    screen.blit(score_surf, score_rect)
    #MW returns current time
    return current_time

#MW moves the screen to make it seem like te player is moving
def drawFlour10(ground_x, ground_y, moveSpeed):
    #MW takes three int values, ground_x which is the x component of the movement, ground_y which is the y portion of the movement, and moveSpeed which is the speed at which the screen moves when the player presses the movement keys
    #MW moves all te different objects in the game as the player presses movement keys to simulates player movement
    #MW Moves the ground rectangles
    ground_rect.y += ground_y
    ground_rect.x += ground_x  
    #MW moves the book item rectangles
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
    
    #Moves every tile in the map matrix
    for tile in tile_list:
        #moves x component of tile rectangle
        tile[1].x += ground_x
        #moves y component of tile rectangle
        tile[1].y += ground_y
        
    #MW checks if there is a collision between the player and one the map tiles
    for tile in tile_list:
        
        #MW checks for the collision
        if player_rect.colliderect(tile[1]):
            #MW if the x component of movement is less than zero all the objects are moved to the right to keep the objects in their original positions as they should not move if the player collides with a tile
            if ground_x < 0:
                ground_rect.x += moveSpeed
                random_book1.x += moveSpeed
                random_book2.x += moveSpeed
                random_book3.x += moveSpeed
                random_book4.x += moveSpeed
                random_book5.x += moveSpeed
                random_book6.x += moveSpeed
                random_book7.x += moveSpeed
                
            #MW if the x component of movement is more than zero all the objects are moved to the left to keep the objects in their original positions as they should not move if the player collides with a tile
            elif ground_x > 0:
                ground_rect.x -= moveSpeed
                random_book1.x -= moveSpeed
                random_book2.x -= moveSpeed
                random_book3.x -= moveSpeed
                random_book4.x -= moveSpeed
                random_book5.x -= moveSpeed
                random_book6.x -= moveSpeed
                random_book7.x -= moveSpeed
            
            #MW if the y component of movement is less than zero all the objects are moved to down to keep the objects in their original positions as they should not move if the player collides with a tile
            if ground_y < 0:
                ground_rect.y += moveSpeed
                random_book1.y += moveSpeed
                random_book2.y += moveSpeed
                random_book3.y += moveSpeed
                random_book4.y += moveSpeed
                random_book5.y += moveSpeed
                random_book6.y += moveSpeed
                random_book7.y += moveSpeed
            
            #MW if the y component of movement is more than zero all the objects are moved to the left to to keep the objects in their original positions as they should not move if the player collides with a tile
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
                #MW if the x component of movement is less than zero all the tiles are moved to the right to move the player object out of collision
                if ground_x < 0:
                    tile[1].x += moveSpeed
                #MW if the x component of movement is more than zero all the tiles are moved to the left to move the player object out of collision
                elif ground_x > 0:
                    tile[1].x -= moveSpeed
                #MW if the x component of movement is less than zero all the tiles are moved to down to move the player object out of collision
                if ground_y < 0:
                    tile[1].y += moveSpeed
                #MW if the y component of movement is more than zero all the tiles are moved up to move the player object out of collision
                elif ground_y > 0:
                    tile[1].y -= moveSpeed 
    
    #MW blits the ground img to the screen as the first layer
    screen.blit(ground,ground_rect)
    
    #MW blits all the map tiles to the screen to generate the map
    for tile in tile_list:
        screen.blit(tile[0],tile[1])
    
#MW changes the player postion depending on what the direction the player should appear to be moving
def movePlayer(player_pos, ground_x, ground_y):
    
    #Changes the player image that is blit onto the screen depending on the direction they are moving
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
    
    #MW if the player is not moving their last positon is what is blit onto the screen
    else:
        if player_pos == 1:
            screen.blit(player_right,player_right_rect)
        
        elif player_pos == 2:
            screen.blit(player_left,player_left_rect)
        
        elif player_pos == 3:
            screen.blit(player_back,player_back_rect)
        
        elif player_pos == 4:
            screen.blit(player_forward,player_forward_rect)
    
    #MW returns the player positon so that it can be reset with the new value
    return player_pos

#MS - Each of these functions responds to whether the initial random book appearance variables are true or false.
#If true, these functions will blit the books onto the screen.
def blueBook():
    if book_apperence1:
        screen.blit(blue_book, random_book1)
        if player_rect.colliderect(random_book1):
            click_e()
#These functions also determine if the player is colliding with the book, if so, the click e function is called. 

def orangeBook():
    if book_apperence2:
        screen.blit(orange_book, random_book2)
        if player_rect.colliderect(random_book2):
            click_e()

def greenBook():
    if book_apperence3:
        screen.blit(green_book, random_book3)
        if player_rect.colliderect(random_book3):
            click_e()

def magentaBook():
    if book_apperence4:
        screen.blit(magenta_book, random_book4)
        if player_rect.colliderect(random_book4):
            click_e()

def tealBook():
    if book_apperence5:
        screen.blit(teal_book, random_book5)
        if player_rect.colliderect(random_book5):
            click_e()
        
def redBook():
    if book_apperence6:
        screen.blit(red_book, random_book6)
        if player_rect.colliderect(random_book6):
            click_e()

def purpleBook():
    if book_apperence7: 
        screen.blit(purple_book, random_book7)
        if player_rect.colliderect(random_book7):
            click_e()


#MS - This function blits the collected books in the top of the screen.
def showBooks(collected_books):
    for i in range(len(collected_books)):
        collected_books[i][1].x = i* tile_size
        collected_books[i][1].y = 0
        screen.blit(collected_books[i][0],collected_books[i][1])

#MS - This matix-list makes up the entirety of the map. 
#It is a really efficient way to blit hundreds of objects without taking up hundreds of lines of code.
#This is really useful when programing colisions. When the player colides with a solid tile, the entire matrix-map is moved.
#In a collision, this moves every element at the same time in the same direction as the player so it appears like the player isn't moving at all.
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

#MW initializes the map
def init_map():
    #MW negative number so that the map is offset to the left
    row_count =-19
    #MW checks each row in the map matrix
    for row in world_data:
        #MW negative number so that the map is offset up
        col_count = -7 
        #MW checks each element in a row of the map matrix
        for tile in row:
            #MW checks what type of tile should be assigned to the map position in accordance to the the number associated with the position in the row
            if tile == 1:
                #MW sets the image that is associated with the number one in the map matrix
                img = pygame.transform.scale(table_img, (tile_size, tile_size))
                #MW sets the rectangle for the image with coordinates that correspond to the col_count and row_count and tile size
                img_rect = img.get_rect(topright = (col_count*tile_size,row_count*tile_size))
                #MW creates a tile image with the image and reactangle
                tile = (img, img_rect)
                #MW appends the tile to the list of all tiles for the map matrix
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
            #MW adds one to column count each time it runs through a element in a row as it is now in the column to the right
            col_count += 1
        #MW adds one to the row count each time it runs through an entire row as it is now one row down
        row_count += 1
    #MW resets the column and row count
    row_count = 0
    col_count = 0
    
init_map()

#MW blits the screen for when the user hhas collected all of ther required books
def game_won():
    screen.fill('White')
    screen.blit(textSurfaceObj3,textRectObj3)
    screen.blit(textSurfaceObj4,textRectObj4)
    screen.blit(textSurfaceObj5,textRectObj5)
    screen.blit(textSurfaceObj6,textRectObj6)

#MW while True game loop
while True:
    #MW for loop that checks events that occur on the display
    for event in pygame.event.get():
        #MW if the x button at the top of the screen is pressed then the game ends
        if event.type == pygame.QUIT:
            pygame.quit()
        #MW if a button is pressed
        if event.type == pygame.KEYDOWN:
            #MW if the a button is pressed then the x portion of movement is set to the movespeed
            if event.key == pygame.K_a: 
                ground_x=moveSpeed
            #MW if the d button is pressed then the x portion of movement is set to the negative movespeed    
            elif event.key == pygame.K_d:
                ground_x=-moveSpeed
            #MW if the w button is pressed then the y portion of movement is set to the movespeed    
            elif event.key == pygame.K_w: 
                ground_y=moveSpeed
            #MW if the s button is pressed then the y portion of movement is set to the negative movespeed      
            elif event.key == pygame.K_s: 
                ground_y=-moveSpeed
        #MW if a button that was pressed is no longer pressed        
        if event.type == pygame.KEYUP:
            #MW sets the x and y components of movement to zero so the player stop moving if the key that was unpressed was w, a, s, or d
            if event.key == pygame.K_a:
                ground_x=0
                
            elif event.key == pygame.K_d:
                ground_x=0
                
            elif event.key == pygame.K_w: 
                ground_y=0
                
            elif event.key == pygame.K_s: 
                ground_y=0
        
        #MS - This checks if the player collides with the first book        
        if player_rect.colliderect(random_book1):
            #MS - This first part checks if a key is being pressed
            if event.type == pygame.KEYDOWN:
                #MS - This check determines if the e key is being pressed.
                if event.key == pygame.K_e:
                    #MW plays sound to signify pickup
                    pickUpSound.play() 
                    #MS - This sets the book1 appearence to false which removes the book from the screen.
                    book_apperence1 = False
                    #MS - This part activates the next random book to appeare randomely
                    book_apperence2 = True
                    #MS - adds book ones image and rectangle to a list that contains the collected books
                    collected_books.append([blue_book,random_book1])
        #MS - Checks if the player has collided with the second book and that book one was collected            
        elif player_rect.colliderect(random_book2) and book_apperence2:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    pickUpSound.play() 
                    book_apperence2 = False
                    book_apperence3 = True
                    collected_books.append([orange_book,random_book2])
        #MS - Checks if the player has collided with the third book and that book two was collected, etc.
        elif player_rect.colliderect(random_book3) and book_apperence3:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    pickUpSound.play() 
                    book_apperence3 = False
                    book_apperence4 = True
                    collected_books.append([green_book,random_book3])    
        elif player_rect.colliderect(random_book4)and book_apperence4:
            pickUpSound.play() 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    book_apperence4 = False
                    book_apperence5 = True
                    collected_books.append([magenta_book,random_book4])     
        elif player_rect.colliderect(random_book5)and book_apperence5:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    pickUpSound.play() 
                    book_apperence5 = False
                    book_apperence6 = True
                    collected_books.append([teal_book,random_book5])
        elif player_rect.colliderect(random_book6)and book_apperence6:
            pickUpSound.play() 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    book_apperence6 = False
                    book_apperence7 = True
                    collected_books.append([red_book,random_book6])            
        elif player_rect.colliderect(random_book7)and book_apperence7:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    pickUpSound.play() 
                    book_apperence7 = False
                    
                    collected_books.append([purple_book,random_book7])
        #MW checks if the user pressed the screen            
        if event.type == pygame.MOUSEBUTTONDOWN:
            #MW checks if the user pressed the start button in the intro
            if textRectObj2.collidepoint(event.pos):
                #MW allows the how to play section of the game to start and the intro section to end
                how_to_play_start = True
                introStart = False
            #MW checks if the user pressed thhe play again button    
            elif textRectObj5.collidepoint(event.pos):
                #starts the game over
                startOver = True
            #MW check if they pressed the no button when asked if they want to restart the game    
            elif textRectObj6.collidepoint(event.pos):
                #MW quits the game
                pygame.quit() 
            #MS - Turns off the how_to_play_start function that I initialized above.
            elif Obj4_text_rect.collidepoint(event.pos):
                controlStart = True
                how_to_play_start = False
                start_time = pygame.time.get_ticks()
    #MW checks a boolean variable for wether or not the intro should be blit onto the screen            
    if introStart:
        #calls the intro function and 
        intro()
    #MW checks if a boolean variable for wether or not the how to play portion of the game shhould be blit onto the screen    
    elif how_to_play_start:
        #calls the how to play function
        how_to_play()
    #MW checks a boolean varaible for wether or not the the main portion of the game should be initiated
    elif controlStart:
        #MW fills the screen a base layer grey
        screen.fill("Grey")
        #MW calls upon all the necessary function for the game to run
        drawFlour10(ground_x, ground_y, moveSpeed)
        player_pos = movePlayer(player_pos, ground_x, ground_y)
        blueBook()
        orangeBook()
        greenBook()
        magentaBook()
        tealBook()
        redBook()
        purpleBook()
        #MW shows all the book you collected at the top left corner of your screen
        showBooks(collected_books)
        #MW gets the score value
        score = display_score()
    
    #MW checks if all the books were collected
    if len(collected_books)==7:
        #MW stop the game functions from running
        controlStart=False
        #MW gets the outro screen and asks the user if they want to play again
        game_won()
        #MW blits how long it took you to collect all the books
        score_message = fontObj1.render(f'your score: {score}',False,"Green")
        score_message_rect = score_message.get_rect(center = (600,450)) 
        screen.blit(score_message,score_message_rect)
        #MW reinitializes all the varaibles so that the game can start again at the exact same state
        if startOver:
            #MW makes it so the user isnt prompted with press e too pick a book in their second playthrough
            timesPlayed +=1
            #MW gets new start time 
            start_time = pygame.time.get_ticks()
            ground_rect.x = -7*tile_size
            ground_rect.y = -18*tile_size
            #MW clears the tile list as their coordinates were all moved around by the player
            tile_list.clear()
            #MW recreates the map
            init_map()
            #resets book apperance so that the first book is once again the only book on the map
            controlStart = True
            book_apperence1 = True
            book_apperence2 = False
            book_apperence3 = False
            book_apperence4 = False
            book_apperence5 = False
            book_apperence6 = False
            book_apperence7 = False
            score = 0
            #MW resets all the books you collected
            collected_books.clear()
            #MW regets all of the random books
            random_book1 = random_blue(blue_book)
            random_book2 = random_orange(orange_book)
            random_book3 = random_green(green_book)
            random_book4 = random_magenta(magenta_book)
            random_book5 = random_teal(teal_book)
            random_book6 = random_red(red_book)
            random_book7 = random_purple(purple_book)
            startOver = False
            
    #MW updates the screen        
    pygame.display.update()
    #MW sets tick count to 60
    clock.tick(60)