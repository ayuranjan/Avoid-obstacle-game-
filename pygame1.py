
import pygame
import sys
import time 
import random

pygame.init() #this iniatializes pygame and all the modules in it . this is the first thing you do
#crash_sound = pygame.mixer.Sound("Wait.mp3")
#pygame.mixer.music.load("Wait.wav")
display_width = 800
display_height = 600
black = (0,0,0) # 3 colours . all color are mixture of rgb = red green blue . total choices = 256 
white = (255,255,255 )
red = (255,0,0)
bird_width = 40
gameDisplay = pygame.display.set_mode((display_width,display_height))# this set the resolution of the display 
pygame.display.set_caption('Bird Racing odds ') #this sets the name of the window opening 
clock = pygame.time.Clock() #we use it for frame per  second
birdImg = pygame.image.load("0.png")#to load image 
background = pygame.image.load("background.png").convert()
def things_dodgeg(count):
    font = pygame.font.SysFont(None ,25 )
    text = font.render("dodged = "+ str(count),True,black)
    gameDisplay.blit(text,(0,0))
def things(thingx,thingy,thingw,thingh,color):#thing x,y corrdinates  witdth height & color 
    pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])  #we use inbuilt draw fn and in that rectangle rect which takes arguments - where we want to draw ,color ,coordinates where to draw , dimension of block 
def bird(x,y):
    gameDisplay.blit(birdImg,(x,y)) # so we are gonna display carImg in coordinates x , y
def text_objects(text,font):
    textSurface =font.render(text,True,red)
    return textSurface ,textSurface.get_rect()



def message_display(text) :
    text_displayed = pygame.font.Font("freesansbold.ttf",115) # we got the text with size and style in which it will be displayed
    text_surface , text_rect = text_objects(text,text_displayed)# it will return text surface and text rectange 
    text_rect.center = ((display_width/ 2),(display_height/2)) #this will centre the text
    gameDisplay.blit(text_surface,text_rect)
    
    pygame.display.update()

    time.sleep(2) # pause why not working?
    game_loop() #to restart the game 

def crash():
    #pygame.mixer.music.stop()
    #pygame.mixer.Sound.play(crash_sound)
    message_display('You crashed ') #message display is a user def fn 

def game_intro():
    intro  =True 
    while intro :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT
                quit()
        gameDisplay.fill(white)

def game_loop():
   #pygame.mixer.music.play(-1) # -1 will play sound in loop  , if n then n times
    x =(display_width  * 0.45)
    y = (display_height *0.8) #in computer the left top of the window is 0,0 and to move down we use y and to move sidways we use x
    x_change  = 0
    thing_startx = random.randrange(0,display_width) 
    thing_starty = -100 # so it will intially outside the window 
    block_speed = 5#how fast thing will move 
    thing_width = 100
    thing_hight = 100
    dodged = 0

    game_exit  = False
    while not game_exit :
        for event in pygame.event.get(): #this creates list of all the events that happened like key is pressed, mouse moved or clicked  etc 
            if event.type == pygame.QUIT: #for the most part is someone hits the x in window popup
                #game_exit =True #to get of loop 
                pygame.quit
                quit()
            elif event.type == pygame.KEYDOWN : #this means if any key is pushed down i.e. pressed
                if event.key == pygame.K_LEFT:#left key is pressed
                    x_change = -15  
                elif event.key  == pygame.K_RIGHT:
                    x_change = 15
            elif event.type == pygame.KEYUP: #pressed key is lifted
                if event.key == pygame.K_LEFT  or event.key == pygame.K_RIGHT:
                    x_change = 0 
        x += x_change
            #print(event)#this will print of the events that happened
            #this all will run in 1 frame per second 
        gameDisplay.fill(red) #it will paint white everwhere
        
            #if we put car before fill ...fill willl paint white over the car
        things(thing_startx,thing_starty,thing_width,thing_hight,black)
        thing_starty = thing_starty + block_speed# block will just move down  
            
        bird(x,y) #to show bird
        things_dodgeg(dodged)
        if x > display_width - bird_width or x < 0:# we subtract car width or else it will exit only when the full car is out of window
            crash()
        if thing_starty > display_height :
            thing_starty = 0 - thing_hight
            thing_startx = random.randrange(0,display_width)
            dodged+= 1 
            block_speed += 1
            thing_width += random.randrange(0,20)
        if y < thing_starty + thing_hight: #y is of bird  so if birds y coordinate is lower than the object it may collide 
            if x > thing_startx and x < thing_startx + thing_width or x + bird_width > thing_startx and x + bird_width < thing_startx + thing_width:
                crash()
        pygame.display.update()#this will update the entire window , if we pass argument inside update() it will update a certain part of window
        clock.tick(60) #this is frame per second ..more the fps the more smooth the window looks 
            #to exit or  quit
        
        
game_loop()
pygame.quit()
quit()


