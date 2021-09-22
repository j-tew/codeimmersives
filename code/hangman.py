from os import system, name
from random_word import RandomWords

###############################################################
###############################################################
### Welcome to my Hangman game!                             ###
### This is just a checklist I was using to build the game. ###
###                                                         ###
### - [X] Create Game Scenes                                ###
### - [X] Create Word Generator                             ###
### - [X] Accept Input for Guesses                          ###
### - [X] Validate Guesses and Update Scene                 ###
###         - Clear Scene After Each Guess                  ###
### - [X] Exchange and Handle Letters on Board              ###
### - [X] Remove wordlist and use RandomWords               ###
###                                                         ###
### **EXTRAS** (Future Updates)                             ###
### - [X] Banner                                            ###
### - [ ] Beginning UI                                      ###
###         - Select Difficulty                             ###
###             - Use phrases instead of words              ###
###         - Categories?                                   ###
###                                                         ###
###############################################################
###############################################################

# Banner
banner = '''
 _   _
| | | | __ _ _ __   __ _ _ __ ___   __ _ _ __
| |_| |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
|  _  | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                   |___/
'''

# Dictionary for the scenes
scene = {
    0: '''
         ___________ 
        |           |
        |
        |
        |
        |
        |
        |
        |
        |
        |
        |
        |''',

    1: '''
         ___________ 
        |           |
        |          ,,,
        |         (X_X)
        |
        |
        |
        |
        |
        |
        |
        |
        |''',

    2: '''
         ___________ 
        |           |
        |          ,,,
        |         (X_X)
        |           |
        |           |
        |
        |
        |
        |
        |
        |
        |''',

    3: '''
         ___________ 
        |           |
        |          ,,,
        |         (X_X)
        |         \_|
        |           |
        |
        |
        |
        |
        |
        |
        |''',

    4: '''
         ___________ 
        |           |
        |          ,,,
        |         (X_X)
        |         \_|_/
        |           |
        |
        |
        |
        |
        |
        |
        |''',

    5: '''
         ___________ 
        |           |
        |          ,,,
        |         (X_X)
        |         \_|_/
        |           |
        |          /
        |         /
        |
        |
        |
        |
        |''',

    6: '''
         ___________ 
        |           |
        |          ,,,
        |         (X_X)
        |         \_|_/
        |           |
        |          / \\
        |         /   \\
        |
        |
        |
        |
        |'''
}

# Credit to ChickenParm for a function to make the game not junk up the terminal
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

# Updating the game board with guesses
def update(brd, wrd, ltr):
    if ltr in wrd:
        num = wrd.count(ltr)
        for i in range(0, num):
            place = wrd.index(ltr)
            brd.pop(place)
            brd.insert(place, ltr)
            wrd = wrd.replace(guess, "-", 1)
    else:
        key += 1
    return wrd, brd

# Selecting a random word.
word = RandomWords().get_random_word()
# testWord = "devildog"
# word = testWord

# Important variables
key = 0
board = list("_" * len(word))
deadWord = ("-" * len(word))

# Game Loop
while word.count("-") < len(word):
    # Keeping the game board clean
    clear()
    print(banner)
    # Hangman scenes
    print(scene[key])
    # Word to be guessed
    print(f"Secret Word: ", *board)
    # If dude is complete, he's dead.
    if key == 6:
        break
    # Take guesses as input
    guess = input(f"\nPlease Enter a Letter: ")
    # Checking guesses and updating the scene and board accordingly
    if len(guess) > 1:
        key += 1
    elif guess in word:
        new = update(board, word, guess)
        board = new[1]
        word = new[0]
    else:
        key += 1
# Ending the Game Loop
if word == deadWord:
    clear()
    print(banner)
    print(scene[key])
    print(f"Secret Word: ", *board)
    print("\tYOU WIN!!!")
else:
    clear()
    print(banner)
    print(scene[6], "GAME OVER!!!")
