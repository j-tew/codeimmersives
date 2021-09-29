from random import choice

def rps():
    choices = {
    "R":
    '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    ''',
    "P":
    '''
        _______
    ---'   ____)____
              ______)
              _______)
              _______)
    ---.__________)
    ''',
    "S":
    '''
        _______
    ---'   ____)____
              ______)
          __________)
          (____)
    ---.__(___)
    '''
    }
    win = "You Win!"
    lose = "You Lose!"
    draw = "It's a tie!"
    comp = choice(list(choices))
    user = input(f"[R]ock, [P]aper, or [S]cissors?\n").upper()
    selections = f"You chose:\n{choices[user]}\nComputer Chose:\n{choices[comp]}"
    if user not in choices:
        print("Invalid Selection")
    elif user == comp:
        print(selections, "\n", draw)
    elif user == "R":
        if comp == "S":
            print(selections, "\n", win)
        else:
            print(selections, "\n", lose)
    elif user == "P":
        if comp == "R":
            print(selections, "\n", win)
        else:
            print(selections, "\n", lose)
    elif user == "S":
        if comp == "P":
            print(selections, "\n", win)
        else:
            print(selections, "\n", lose)

rps()

