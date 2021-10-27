#learning while loop 

#control the main game 
#put game instructions here

import random
Flag=True
answer = input ("Do you want to play a game?")
while 'y' in answer :
    counter=10
    number=random.randrange(1,100)
    while(Flag and counter >0):
        guess= input("guess a number bwteen 1 and 100: ")
        try:
            int(guess)
            check=True
        except ValueError:
            check=False

        if(check):
            if guess == number :
                print ("you won")
                Flag=False
            
            else:
                print("you need to guess again")
                counter=counter-1
        

    answer = input("Do you want to play agian?")
print("thank you for playing the game")
    
        
    