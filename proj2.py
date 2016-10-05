"""
Title: Project 1
Abstract: Text Based Game
Name: Akoni Morrison
Date: 10/5/2016
"""
import random
import time
 
print("Hello")
time.sleep(2) #makes program wait a vertain amount of time
print("There")
def displayIntro():
    print("It is the end of a long year of fighting dragons")
    print("you come toe the crossroads on your trip home, one path leads home")
    print("where you will be rewarded for the dragons you've killed")
    print("and the other leads through a forest where you can be mauled by bears")
    print()
def choosePath():
    path = "" #path = empty string
    while path != "1" and path != "2": #input validation
        path = input("Which path will you choose? (1 or 2): ")

    return path
def checkPath(chosenPath):
    print("You head down the path")
    time.sleep(2)
    print("There's a boulder nearby that looks familiar, that must be a good sign")
    print("But your skin begins to tingle...")
    print()
    time.sleep(2)

    correctPath = random.randint(1, 2)
    if chosenPath == str(correctPath):
        print("That tingling was just the feeling of admiration from the citizens")
        print("Welcome back home!")
    else:
        print("A pack of large bears jump out at you")
        print("They start tearing your body apart")
        print("There is no record left of your existence")




playAgain = "yes"
while playAgain == "yes" or playAgain == "y":
    displayIntro()
    choice = choosePath()
    checkPath(choice) # choice is equal to "1" or "2"
    playAgain = input("Do you want to play again? (yes or y to continue playing): ")
