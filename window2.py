#Alex Ladin

import pygame as py, os, random, time

os.system ('cls')

py.init()
black = (0, 0, 0)
white = (255, 255, 255)
messages=["ScreenSize", "Background Color", "Object Color", "Sounds on/off"]
width = 800
height = 800

window = py.display.set_mode((width, height))
py.display.set_caption("settings")


title_font = py.font.SysFont("arial", 80)
subtitle_font = py.font.SysFont("arial", 50, italic = True)
wbox=25
hbox=25
square = py.Rect(10,10, wbox,hbox)
def display_title(message):
    py.time.delay(100)
    text = title_font.render(message, 1, white)
    window.blit(text, (width/2 - text.get_width()/2, 70))
    py.display.flip()
    py.time.delay(100)
# def display_subtitle(message, x, y):
#     py.time.delay(100)
#     text = subtitle_font.render(message, 1, white)
#     window.blit(text, (x, y))
#     py.display.flip()
#     py.time.delay(100)

def display_Menu():
    x=70
    y=190
    square.x=x
    square.y=y
    for i in range(0, len(messages)):
        word= messages[i]
        py.draw.rect(window,white, square )
        text=subtitle_font.render(word, 1, white)
        window.blit(text, (x+wbox+10, y))
        py.display.flip()
        py.time.delay(100)
        y +=100
        square.y=y
run = True
while run:
    for eve in py.event.get():
        if eve.type == py.QUIT:
            run = False
            py.quit()
    display_title("settings")
    py.time.delay(300)
    

    # display_subtitle("window size",80, 150)
    # py.time.delay(300)
    # display_subtitle("background color", 80, 250)
    # py.time.delay(300)
    # display_subtitle("object colors", 80, 350)
    # py.time.delay(300)
    # display_subtitle("sound (on/off)", 80, 450)
    # py.time.delay(300)


    display_Menu()
    print(py.mouse.get_pos())
py.quit()