#for learning
import random
import time as t
#Rock Paper Scissors Game
def game():
    #Setting the options for the game
    options = ["rock", "paper", "scissors"]
    #Creating random option from bot side to face the user side
    bot = random.choice(options)
    #Asking input from the user 
    user=str(input("Enter your play: "))
    #Making it a bit thrilling by making user wait for a bit. Haha. 
    t.sleep(0.2)
    print("BOT:", bot)
    #All logics and conditions for the game
    if user == bot:
        print("tie")
    elif user == "paper":
        if bot == "scissors":
            print("User lost! Scissors cut the paper")
        elif bot == "rock":
            print ("User won! Paper wraps the rock !@")
    elif user == "rock":
        if bot == "scissors":
            print("User won! Rock destroys the scissors")
        elif bot == "paper":
            print ("User lost! Paper wraps the rock !@") 
    elif user == "scissors" :
        if bot == "paper":
            print("User won! Scissors cuts paper!!")
        elif bot == "rock":
            print("User lost! Rock bangs scissors!@")
    repeat= str(input("Do you want to continue?, Press ,'y' for yes or, 'n' for no !" ))
    if repeat=="y" or repeat=="Y":
        print("Welcome to the game, again....")
        #Calling game function again for replaying the game if user wants to...
        game()
        
    else:
        print("BYE BYE")
 #Executing the game finally.....       
game() 
















    

