from os import system, name
import random

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
###                                                         ###
### **EXTRAS** (Future Updates)                             ###
### - [ ] Banner                                            ###
### - [ ] Beginning UI                                      ###
###         - Select Difficulty                             ###
###                                                         ###
###############################################################
###############################################################

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
# Sample wordlist (use RandomWords in the future?)
wordlist = (
    "apt", "ask", "bat", "bad", "bag", "cat", "cap", "cab", "dad", "dab", "fan", "fat", "fad", "gap", "gab", "gal",
    "gas", "ham", "has", "had", "hat", "jab", "jam", "lab", "lad", "lag", "lap", "man", "mad", "mat", "nap", "pan", "pad",
    "pal", "ran", "ram", "rag", "rat", "sad", "sag", "sat", "sap", "tab", "tan", "tad", "tag", "tap", "van", "vat", "yam", "zap"
)

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

# Selecting a word from the wordlist above.
# Update to better method later.
word = random.choice(wordlist)
#testWord = "devildog"
key = 0
board = list("_" * len(word))
deadWord = ("-" * len(word))

# Game Loop
while word.count("-") < len(word):
    # Keeping the game board clean
    clear()
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
    print(scene[key])
    print("\tYOU WIN!!!")
else:
    clear()
    print(scene[6], "GAME OVER!!!")