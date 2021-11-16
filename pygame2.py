#Alex Ladin 
#11/11/21
#Game design 


import os
import pygame as py, time, sys

py.init()
py.time.delay(100)


width=800
height=600

colors= {'red':(150,0,0), 'green': (0,200,0), 'blue':(0,0,255), 'purple':(150, 0, 150), 'white':(255,255,255), 'black':(0,0,0)}
screen=py.display.set_mode((width,height))
bg=py.image.load('GameImages\\bgSmaller.jpg')
screen.blit(bg,(0,0))
py.display.flip()
guyx=200
guyy=300
guy=py.image.load("GameImages\Pygame-Tutorials-master\Game\R1.png")
screen.blit(guy, (guyx, guyy))
py.display.flip()
myColor=colors.get('purple')
py.display.flip()
green=colors.get('green')
red=colors.get('red')
blue=colors.get('blue')


x=width/2
y=height/2
wbox=50
hbox=50
boldX=width-300
boldY=height-200

screen.fill(green)
py.display.set_caption("Alex's Window")

boulder=py.Rect(boldX,boldY,100,200)
rect = py.Rect(x, y, hbox, wbox)
COUNT = 10
jumpCount = COUNT
Jump = False 
run=True
while run:
    for ev in py.event.get():
        if ev.type == py.QUIT:
            run=False

        speed = 2 
        keyBoardkey = py.key.get_pressed()
    if keyBoardkey [py.K_LEFT]:
        print(boulder.x)
        print(guyx)
        guyx -= speed
    if keyBoardkey [py.K_RIGHT] :  # and guyx < boulder.x-45
        print(boulder.x)
        print(guyx)
        guyx += speed
    if not Jump:
        if keyBoardkey[py.K_UP]:
            guyy -= speed
        if keyBoardkey[py.K_DOWN]:
            guyy += speed
        if keyBoardkey[py.K_SPACE]:
            Jump = True
    else:
        if jumpCount>=-COUNT:
            rect.y-= jumpCount*abs(jumpCount)/2
            guyy-= jumpCount*abs(jumpCount)/2
            jumpCount -=1

        else:
            jumpCount=COUNT
            Jump=False

            #Setting Boundaries
        


        if rect.y > height - hbox : rect.y = height - hbox
        if guyy > height - hbox : guyy = height - hbox


     
    screen.blit(bg,(0,0))
    screen.blit(guy, (guyx, guyy))
    # py.draw.rect(screen,(red),rect)
    py.draw.rect(screen,red,boulder)
    py.display.flip()
    py.time.delay(30)