#Alex Ladin
#10/27/21

import pygame as py, os, random, time
py.init()
BLACK=(153,255,255)
WHITE=(0,0,0)
PURPLE=(255,204,255)
WIDTH = 800
HEIGHT = 800
messages=['Instructions','Level 1','Level 2','Settings','Score Board', 'Exit']
messages2=['Screen size', 'Object Color', 'Sound on/off', 'Back']
Ssmessages=['Larger', 'Smaller', 'Back']
instructions_messages=['in this game we are trying to make the circle eat the square']
win=py.display.set_mode((WIDTH,HEIGHT))
py.display.set_caption("Setting Window")
#TITLE_FONT= py.font.SysFont(name,size,bold=false, italic= false)
TITLE_FONT= py.font.SysFont('Times new roman', 70, italic=True)
SUBTITLE_FONT= py.font.SysFont('Times new roman', 50, italic=True)
xbox=25
wbox=25
square=py.Rect(10,10, wbox, xbox)
70-95, 485-515
def display_message(message, y):
    py.time.delay(100)
    text=TITLE_FONT.render(message,30, BLACK )
    win.blit(text, (WIDTH/2-text.get_width()/2, y) )
    py.display.update()
    py.time.delay(10)

def displaySub(subTitle,ysub):
    py.time.delay(100)
    text=SUBTITLE_FONT.render(subTitle,1, BLACK )
    win.blit(text, (10, ysub ))
    py.display.update()
    py.time.delay(10)


def display_Menu(menuMes):
    x=70
    y=190
    square.x=x
    square.y=y
    for i in range(0, len(menuMes)):
        word= menuMes[i]
        py.draw.rect(win, PURPLE, square)
        text=SUBTITLE_FONT.render(word,10, BLACK)
        win.blit(text, (x+wbox+10, y))
        py.display.flip()
        py.time.delay(100)
        y += 100
        square.y=y
        py.display.set_caption("Menu Window")

win.fill(WHITE)
display_message('Menu', 40)
ysub=200
py.time.delay(200)
display_Menu(messages)
run=True

while run:
    for eve in py.event.get():
        if eve.type == py.QUIT:
            run=False

    if eve.type==py.MOUSEBUTTONDOWN:
        mouse_pressed=py.mouse.get_pressed()
        if mouse_pressed[0]:
            mouse_pos=py.mouse.get_pos()
            print(mouse_pos)
            if mouse_pos[0]>=70 and mouse_pos[0]<=95 and mouse_pos[1]>490 and mouse_pos[1]<515:
                win.fill(WHITE)
                display_message("Settings", 40)
                py.display.set_caption("Setting Window")
                mouse_pos=py.mouse.get_pos()
                #if mouse_pos==true:

                display_Menu(messages2)
                
            if mouse_pos[0]>70 and mouse_pos[0]<=95 and mouse_pos[1]>185 and mouse_pos[1]<=215:
                win.fill(WHITE)
                display_message('Screen Size', 40)
                py.display.set_caption("Screen Size Window")
                display_Menu(Ssmessages)
                

            if mouse_pos[0]>70 and mouse_pos[0]<=95 and mouse_pos[1]>200 and mouse_pos[1]<=85:
                win.fill(WHITE)
                display_message('instruction', 40)
                display_message('back', HEIGHT-100)
                py.display.set_caption("This is our game ")
                mouse_pos

            if mouse_pos[0]>70 and mouse_pos[0]<=95 and mouse_pos[1]>200 and mouse_pos[1]<=85:
                win.fill(WHITE)
                display_message('sound on/off', 40)
                display_message('back', HEIGHT-100)
                mouse_pos

            if mouse_pos[0]>70 and mouse_pos[0]<=95 and mouse_pos[1]>200 and mouse_pos[1]<=85:
                win.fill(WHITE)
                display_message('sound on/off', 40)
                display_message('back', HEIGHT-100)
                mouse_pos

            

            
            
                

            


                