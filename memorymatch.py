import random , pygame, os, array

#Alex Ladin 
#11/18/2021
#this is my version of the code that i can break 
#https://github.com/mathmaniac88/memory-pygame


#Load modules and initialize display
import os, random, time, pygame
pygame.init()
SCREEN = (600,500)
screen=pygame.display.set_mode(SCREEN)
ICON = pygame.image.load(os.path.join("Images\\Pygame-Tutorials-master\Game\Screenshot 2021-11-30 090922.png"))
pygame.display.set_icon(ICON)
pygame.display.set_caption("Memory")
#DISPLAY = pygame.display.set_mode(SCREEN)
Images= ["Images\\Pygame-Tutorials-master\Game\\apple .png", "Images\Pygame-Tutorials-master\Game\\apple .png", "Images\Pygame-Tutorials-master\Game\\banana.png", "Images\Pygame-Tutorials-master\Game\\banana.png", "Images\Pygame-Tutorials-master\Game\\cherry.png", "Images\Pygame-Tutorials-master\Game\\cherry.png", "Images\Pygame-Tutorials-master\Game\\grape.png", "Images\Pygame-Tutorials-master\Game\\grape.png", "Images\Pygame-Tutorials-master\Game\\lemon.png", "Images\Pygame-Tutorials-master\Game\\lemon.png", "Images\Pygame-Tutorials-master\Game\\orange.png", "Images\Pygame-Tutorials-master\Game\\orange.png", "Images\Pygame-Tutorials-master\Game\\pear.png", "Images\Pygame-Tutorials-master\Game\\pear.png", "Images\Pygame-Tutorials-master\Game\\pineapple.png", "Images\Pygame-Tutorials-master\Game\\pineapple.png", "Images\Pygame-Tutorials-master\Game\\strawberry.png", "Images\Pygame-Tutorials-master\Game\\strawberry.png", "Images\Pygame-Tutorials-master\Game\\watermelon.png", "Images\Pygame-Tutorials-master\Game\\watermelon.png"]
Frontcard="Images\Pygame-Tutorials-master\Game\\card front good.png"
shuffleimages=random.shuffle(Images)
#put the double array here? 
images=len(Images)
#print(images)
Cards=[0,0]
print(Cards)

#i think i need to add a list here with all of my new images 
#i also need to find out where in this code they are putting the numbers 


#Define objects and generate number grid
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
ARIAL_200 = pygame.font.SysFont("Arial", 200)
ARIAL_50 = pygame.font.SysFont("Arial", 50)
ARIAL_35 = pygame.font.SysFont("Arial", 35)
ARIAL_20 = pygame.font.SysFont("Arial", 20)
CARD_LEN = 100
CARD_MARGIN = 10
CARD_HOR_PAD = 37
CARD_VER_PAD = 22
ROWS = 4
COLS = 5
DEFAULT_IMAGE_SIZE=(100,100)
xm=0
ym=0
#cards = [i for i in range(10) for j in range(2)]
#random.shuffle(cards)
screen.fill(GREEN)
# for i in range(images):
#     y=10
#     counter=0
#     for j in range (ROWS):
#         x=10
#         for k in range (COLS):
#             Card=pygame.image.load(Images[counter])
#             Card = pygame.transform.scale(Card, DEFAULT_IMAGE_SIZE)
#             screen.blit(Card,(x,y))
#             x+=120
#             counter+=1
#         y+=120
for i in range(images):
    y=10
    for j in range (ROWS):
        x=10
        for k in range (COLS):
            rect=pygame.Rect(x,y , 100, 100 )
            pygame.draw.rect(screen, BLACK, rect)    
            x+=120
            pygame.display.flip()
        y+=120

y=10
for j in range (ROWS):
    x=10
    for k in range (COLS):
        frcard=pygame.image.load(Frontcard)
        frcard = pygame.transform.scale(frcard, DEFAULT_IMAGE_SIZE)
        screen.blit(frcard,(x,y))
        x+=120

    y+=120

pygame.display.flip()
rect=pygame.Rect(10, 10, 100, 100 )
pygame.draw.rect(screen, BLACK, rect)

#for j in range (ROWS):
    #pygame.draw.rect(x,y)
    
Card1=True
Card2=True

run=True

while run:
    for event in pygame.event.get():
        #Detect quit
        if event.type == pygame.QUIT:
            run=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            mouse_pressed = pygame.mouse.get_pressed()
            if mouse_pressed[0]:
                mouse_pos =pygame.mouse.get_pos()
                # print(pygame.mouse.get_pos())
                xm=mouse_pos[0]
                ym=mouse_pos[1]

        if xm >14 and xm<100 and ym>14 and ym<100:
            
        #collide = pygame.Rect.collidepoint(rect,(xm,ym))
        #collide function
            if Card1:
                print("Card 1")
                Cards[0]=0
                Card1=False
                print(Cards)
            elif Card2:
                Cards[1]=0
                Card2=False
            
        if xm >135 and xm<220 and ym>14 and ym<100:
            # print("card2")
          
        #collide function
            if Card1:
                print("card1")
                Cards[0]=1
                Card1=False
            elif Card2:
                print("card2")
                Cards[1]=1
                Card2=False
                print(Cards)
                
            
        if xm >256 and xm<337 and ym>14 and ym<100:
        
           
        #collide function
            if  Card1:
                Cards[0]=2
                Card1=False
            elif Card2:
                Cards[1]=2
                Card2=False

        if xm >375 and xm<459 and ym>14 and ym<100:
        
            collide = pygame.Rect.collidepoint(rect,(xm,ym))
        #collide function
            if collide and Card1:
                Cards[0]=3
                Card1=False
            elif collide and Card2:
                Cards[1]=3
                Card2=False

        if xm >499 and xm<583 and ym>14 and ym<100:
            
            collide = pygame.Rect.collidepoint(rect,(xm,ym))
        #collide function
            if collide and Card1:
                Cards[0]=4
                Card1=False
            elif collide and Card2:
                Cards[1]=4
                Card2=False

        if xm >17 and xm<101 and ym>136 and ym<220:
            
            collide = pygame.Rect.collidepoint(rect,(xm,ym))
    #collide function
            if collide and Card1:
                Cards[0]=5
                Card1=False
            elif collide and Card2:
                Cards[1]=5
                Card2=False

        if xm >138 and xm<219 and ym>136 and ym<220:
            
            collide = pygame.Rect.collidepoint(rect,(xm,ym))
        #collide function
            if collide and Card1:
                Cards[0]=6
                Card1=False
            elif collide and Card2:
                Cards[1]=6
                Card2=False

        if xm >257 and xm<343 and ym>136 and ym<220:
            
            collide = pygame.Rect.collidepoint(rect,(xm,ym))
        #collide function
            if collide and Card1:
                Cards[0]=7
                Card1=False
            elif collide and Card2:
                Cards[1]=7
                Card2=False

        if xm >375 and xm<436 and ym>136 and ym<220:
            
            collide = pygame.Rect.collidepoint(rect,(xm,ym))
        #collide function
            if collide and Card1:
                Cards[0]=8
                Card1=False
            elif collide and Card2:
                Cards[1]=8
                Card2=False
        
        if xm >496 and xm<582 and ym>136 and ym<220:
            
            collide = pygame.Rect.collidepoint(rect,(xm,ym))
        #collide function
            if collide and Card1:
                Cards[0]=9
                Card1=False
            elif collide and Card2:
                Cards[1]=9
                Card2=False

        if xm >14 and xm<103 and ym>256 and ym<342:
            
            collide = pygame.Rect.collidepoint(rect,(xm,ym))
        #collide function
            if collide and Card1:
                Cards[0]=10
                Card1=False
            elif collide and Card2:
                Cards[1]=10
                Card2=False

        if xm >139 and xm<221 and ym>256 and ym<342:
            
            collide = pygame.Rect.collidepoint(rect,(xm,ym))
        #collide function
            if collide and Card1:
                Cards[0]=11
                Card1=False
            elif collide and Card2:
                Cards[1]=11
                Card2=False

        if xm >256 and xm<345 and ym>256 and ym<342:
            
            collide = pygame.Rect.collidepoint(rect,(xm,ym))
        #collide function
            if collide and Card1:
                Cards[0]=12
                Card1=False
            elif collide and Card2:
                Cards[1]=12
                Card2=False

        if xm >375 and xm<460 and ym>256 and ym<342:
            
            collide = pygame.Rect.collidepoint(rect,(xm,ym))
        #collide function
            if collide and Card1:
                Cards[0]=13
                Card1=False
            elif collide and Card2:
                Cards[1]=13
                Card2=False

        if xm >495 and xm<584 and ym>256 and ym<342:
            
            collide = pygame.Rect.collidepoint(rect,(xm,ym))
        #collide function
            if collide and Card1:
                Cards[0]=14
                Card1=False
            elif collide and Card2:
                Cards[1]=14
                Card2=False

        if xm >14 and xm<102 and ym>374 and ym<463:
            
            collide = pygame.Rect.collidepoint(rect,(xm,ym))
        #collide function
            if collide and Card1:
                Cards[0]=15
                Card1=False
            elif collide and Card2:
                Cards[1]=15
                Card2=False

        if xm >134 and xm<221 and ym>374 and ym<463:
            
            collide = pygame.Rect.collidepoint(rect,(xm,ym))
        #collide function
            if collide and Card1:
                Cards[0]=16
                Card1=False
            elif collide and Card2:
                Cards[1]=16
                Card2=False
        
        if xm >258 and xm<373 and ym>374 and ym<463:
            
            collide = pygame.Rect.collidepoint(rect,(xm,ym))
        #collide function
            if collide and Card1:
                Cards[0]=17
                Card1=False
            elif collide and Card2:
                Cards[1]=17
                Card2=False

        if xm >377 and xm<460 and ym>374 and ym<463:
            
            collide = pygame.Rect.collidepoint(rect,(xm,ym))
        #collide function
            if collide and Card1:
                Cards[0]=18
                Card1=False
            elif collide and Card2:
                Cards[1]=18
                Card2=False

        if xm >498 and xm<581 and ym>374 and ym<463:
            
            collide = pygame.Rect.collidepoint(rect,(xm,ym))
        #collide function
            if collide and Card1:
                Cards[0]=19
                Card1=False
            elif collide and Card2:
                Cards[1]=19
                Card2=False
        print(Cards[0],Cards[1])
        xm=0
        ym=0
        y=10
        for j in range (ROWS):
            x=10
            for k in range (COLS):
                frcard=pygame.image.load(Frontcard)
                frcard = pygame.transform.scale(frcard, DEFAULT_IMAGE_SIZE)
                screen.blit(frcard,(x,y))
                x+=120

            y+=120

    #keep going with every other card

pygame.quit()


