import pygame, math, random, sys, time, os

os.system('cls')
pygame.init()

#create our screen or window

WIDTH=800
HEIGHT=500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game!")
#Define Colors
WHITE= [255, 255, 255]
BLACK= [0, 0, 0]

#load images
images= []
screen.fill(WHITE)
pygame.display.update()
for i in range(7):
    image=pygame.image.load("ImagesHM\\hangman" + str(i)+ ".png")
    images.append(image)
    screen.blit(images[i], (80,100))
    pygame.display.update()
    pygame.time.delay(500)
#set up fonts
gameWords= ['python','java','trackpad','computer','keyboard','geeks','laptop','headphones','charger','mouse','software','hardware']
TitleFont = pygame.font.SysFont("comicsans", 70)
WordFont= pygame.font.SysFont ("comicans", 50)
#function to update game and screen
def updateScree(word, turns):
    screen.fill(WHITE)
    pygame.display.update()
def updateWord(word, guesses, turns):  # function with a parameter to update word
    global displayWord="" 
    for char in word: 
        if char in guesses: 
            print(char,end=' ') 
        else: 
            print('_', end =' ')
    textW=WordFont.render(displayWord, 1, BLACK)
    screen.blit(textW, (350, 150))
    screen.blit(images[i], (80,100))
text=TitleFont.render("HANGMAN",1, BLACK)
centerTitle=WIDTH/2-text.get_width()/2 #gets the width on the screen/2 - width of our text/2

screen.blit(text, (centerTitle,20))
pygame.display.update()
check = True
while check:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            check = False
        word=random.choice(gameWords) 
        counter=len(word) 
        print(counter) 
        print (word)    #delete when we finish the code 
        turns= 0   #should we conider controlling this number when he/she misses 
        updateScreen(word, turns)
        guesses='' 
        while turns<7 and counter >0:
            newGuess=input("\n\n Give me a letter ") 
            #check that the new letter has not been used before 
        if newGuess not in guesses: 
            if newGuess not in word: 
                turns +=1    #       turns = turns -1 
                print("Wrong! You have  ", turns, "guesses left") 
            else: 
                counter -=word.count(newGuess) #deleten repeated letters 
                print("nice guess!") 
            guesses += newGuess  
        else: 
            print("you used this one already") 
        updateWord(word, guesses, turns) 
pygame.quit()
sys.exit()