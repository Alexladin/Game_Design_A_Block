#Alex Ladin
#learning how to use windows and make a menu 
#11/1/21

import pygame as py, os, random, time
py.init()
BLACK=(178,255,102)
WHITE=(204,0,204)
PURPLE=(204,153,205)
WIDTH = 800
HEIGHT = 800
bmessages=["Back"]
messages=['Instructions','Level 1','Level 2','Settings','Score Board', 'Exit']
messages2=['Screen size', 'Object Color', 'Sound on/off', ]
Ssmessages=['Larger', 'Smaller', ]
imessages=["In order to win you need to make the circle eat the square"]
win=py.display.set_mode((WIDTH,HEIGHT))
py.display.set_caption("Setting Window")
#TITLE_FONT= py.font.SysFont(name,size,bold=false, italic= false)
TITLE_FONT= py.font.SysFont('times new roman', 70, )
SUBTITLE_FONT= py.font.SysFont('times new roman', 50, )
xbox=25
wbox=25
square=py.Rect(10,10, wbox, xbox)

def display_message(message):
    py.time.delay(100)
    text=TITLE_FONT.render(message,30, BLACK )
    win.blit(text, (WIDTH/2-text.get_width()/2, 30) )
    py.display.update()
    py.time.delay(10)

def displaySub(subTitle,ysub):
    py.time.delay(100)
    text=SUBTITLE_FONT.render(subTitle,1, BLACK )
    win.blit(text, (10, ysub ))
    py.display.update()
    py.time.delay(10)

def display_back():
                x=660
                y=730
                square.x=x
                square.y=y
                for i in range(0,len(bmessages)):
                    word= bmessages[i]
                    py.draw.rect(win, PURPLE, square)
                    text=SUBTITLE_FONT.render(word,10, BLACK)
                    win.blit(text, (x+wbox+10, y))
                    py.display.flip()
                    
                    
                    square.y=y


def display_Menu():
    x=70
    y=190
    square.x=x
    square.y=y
    for i in range(0, len(messages)):
        word= messages[i]
        py.draw.rect(win, PURPLE, square)
        text=SUBTITLE_FONT.render(word,10, BLACK)
        win.blit(text, (x+wbox+10, y))
        py.display.flip()
        py.time.delay(100)
        y += 100
        square.y=y
        py.display.set_caption("Menu Window")

win.fill(WHITE)
display_message('Menu')
ysub=200
py.time.delay(200)
display_Menu()
display_back()
run=True
counter=1
back=1
while run:
    
    for eve in py.event.get():
        if eve.type == py.QUIT:
            run=False

    if eve.type==py.MOUSEBUTTONDOWN:
        mouse_pressed=py.mouse.get_pressed()
        if mouse_pressed[0]:
            mouse_pos=py.mouse.get_pos()
            print(mouse_pos)
            if mouse_pos[0]>=70 and mouse_pos[0]<=95 and mouse_pos[1]>490 and mouse_pos[1]<515 and counter==1:
                win.fill(WHITE)
                display_message("Settings")
                py.display.set_caption("Setting Window")
                mouse_pos=py.mouse.get_pos()
                counter +=1
                
                x=70
                y=190
                square.x=x
                square.y=y
                for i in range(0, len(messages2)):
                    word= messages2[i]
                    py.draw.rect(win, PURPLE, square)
                    text=SUBTITLE_FONT.render(word,10, BLACK)
                    win.blit(text, (x+wbox+10, y))
                    py.display.flip()
                    py.time.delay(100)
                    y += 100
                    square.y=y

                x=660
                y=730
                square.x=x
                square.y=y
                for i in range(0, len(back)):
                    word= back[i]
                    py.draw.rect(win, PURPLE, square)
                    text=SUBTITLE_FONT.render(word,10, BLACK)
                    win.blit(text, (x+wbox+10, y))
                    py.display.flip()
                    
                    
                    square.y=y            

            if mouse_pos[0]>70 and mouse_pos[0]<=95 and mouse_pos[1]>185 and mouse_pos[1]<=215 and counter==1:
                win.fill(WHITE)
                display_message('Instructions')
                display_message('this is our game', HEIGHT-100)
                py.display.set_caption("instructions window")
                x=70
                y=190
                square.x=x
                square.y=y
                
                for i in range(0, len(imessages)):
                    word= imessages[i]
                    py.draw.rect(win, PURPLE, square)
                    text=SUBTITLE_FONT.render(word,10, BLACK)
                    win.blit(text, (x+wbox+10, y))
                    py.display.flip()
                    py.time.delay(100)
                    y += 100
                    square.y=y
            
            
            if mouse_pos[0]>70 and mouse_pos[0]<=95 and mouse_pos[1]>185 and mouse_pos[1]<=215 and counter==2:
                win.fill(WHITE)
                display_message('Screen Size')
                py.display.set_caption("Screen Size Window")
                x=70
                y=190
                square.x=x
                square.y=y
                for i in range(0, len(Ssmessages)):
                    word= Ssmessages[i]
                    py.draw.rect(win, PURPLE, square)
                    text=SUBTITLE_FONT.render(word,10, BLACK)
                    win.blit(text, (x+wbox+10, y))
                    py.display.flip()
                    py.time.delay(100)
                    y += 100
                    square.y=y

            
              
                    
                            
                
        
               
          
                    
                            
                                

            print(counter)
            print(back)

                    

                    