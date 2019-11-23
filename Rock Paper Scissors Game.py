#This program is to make a game rock, paper, scissor!

from random import randint

startgame = 1

while startgame == 1:
    player1 = input("Pick rock, paper, or scissors!")

    if player1 == "rock" or player1 == "paper" or player1 == "scissors":
        print("Player chose " + player1 + ".")
    else:
        print("Please pick rock, paper or scissors!")

    #This will make the computer randomly pick a number associated with rock paper and scissors!    
    computer = randint(1,3)
    if computer == 1:
        computer = "rock"
    elif computer == 2:
        computer = "paper"
    else:
        computer = "scissors"

    print("Computer chose " + computer + ".")

    #Now to determine who wins! Player or Computer!

    if player1 == "rock" and computer == "rock":
        print("Draw!")
    elif player1 == "rock" and computer == "paper":
        print("Computer wins!")
    elif player1 == "rock" and computer == "scissors":
        print("Player wins!")
    elif player1 == "paper" and computer == "rock":
        print("Player wins!")
    elif player1 == "paper" and computer == "paper":
        print("Draw!")
    elif player1 == "paper" and computer == "scissors":
        print("Computer wins!")
    elif player1 == "scissors" and computer == "rock":
        print("Computer wins!")
    elif player1 == "scissors" and computer == "paper":
        print("Player wins!")
    elif player1 == "scissors" and computer == "scissors":
        print("Draw!")

    startgame = input("Would you like to play again? (Yes:1 No:0)")


