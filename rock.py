# rock paper and scissors
from random import randint



print("Welcome to Rock, Paper and Scissors")


choices = ['rock', 'paper', 'scissors']
while True:
    computer = choices[randint(0,2)]
    player = input("rock, paper, or scissors? (or end the game)").lower()
    if player == "end the game":
        print("The game has ended.")
        break
    elif player == computer:
         print("Tie!")
    elif player == "rock":
        if computer == "paper":
           print("computer: ",computer)
           print("player: ",player)
           print("You Lose")
        if computer == "scissors":
           print("computer: ",computer)
           print("player: ",player)
           print("You win")
    elif player == "paper":
        if computer == "rock":
           print("computer: ",computer)
           print("player: ",player)
           print("You win")
        if computer == "scissors":
           print("computer: ",computer)
           print("player: ",player)
           print("You Lose")
    elif player == "scissors":
        if computer == "paper":
           print("computer: ",computer)
           print("player: ",player)
           print("You win")
        if computer == "rock":
           print("computer: ",computer)
           print("player: ",player)
           print("You Lose")

    

    
