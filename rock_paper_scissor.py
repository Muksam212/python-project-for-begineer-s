from random import randint

#create a list of player option

t = ['Rock', 'Paper', 'Scissor']

computer = t[randint(0, 2)]

player = False

while player == False:
    player = input("Rock, Paper, Scissor?")

    if player == computer:
        print("Tie")
    elif player == "Rock":
        if computer == "Paper":
            print("You Lose!!", computer, "Covers", player)
        else:
            print("You won!", player, "smashes", computer)

    elif player == "Paper":
        if computer == "Scissor":
            print("You loose")
        else:
            print("You win")

    elif player == "Scissor":
        if computer == "Rock":
            print("You loose", computer, "Smashes", player)
        else:
            print("You win!!", player, "cut", computer)

    else:
        print("There is not a valid move")

    player = False
    computer = t[randint(0, 2)]