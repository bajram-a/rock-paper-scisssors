import random
def playerChoice():
    while True:
        print("Please choose rock, paper or scissors: ")
        x = input().lower()
        if x == "rock":
            return 1
        elif x == "paper":
            return 2
        elif x == "scissors":
            return 3

def computerChoice():
    return random.randint(1,3)

def choiceStr(x):
    if x == 1:
        return "rock"
    elif x == 2:
        return "paper"
    elif x == 3:
        return "scissors"

def winner(a, b):
    print("Computer played {} and you played {}.".format(choiceStr(b), choiceStr(a)))
    if a == b:
        print("It's a draw!")
    elif a == 1 and b == 3 or a == 2 and b == 1 or a == 3 and b == 2:
        print("You win!")
    else:
        print("You lose!")

def play():
    winner(playerChoice(), computerChoice())
    print("\nDo you want to play again? Y/N")
    a = input().lower()
    if a == "y":
        play()
    else:
        print("Thank you for playing. ")
        return

play()

