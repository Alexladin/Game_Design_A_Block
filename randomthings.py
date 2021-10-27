#AlexLadin
#9/15/21

#We are going to learn how to use random numbers
#Make a guess number game 

import os
import random

os.system('cls')
random.seed(20)
#this for loop was to play with random numbers
for i in range(10):
    randy= random.randint(3,5)
    print(randy)
    randy2=random.random()
    randy2 *=100
    print(int(randy2))

#arrays in python are called lists 
fruits=["apple", "banana", "Berries"]
MyFruit= random.choices(fruits)
print(MyFruit)