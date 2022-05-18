# Create a function that takes in a word and a list.
# The list contains random letters.
# The function should return TRUE if the list contains the correct
# amount of letters to complete the word.

from string import ascii_lowercase

word = 'disassemble'
l1 = ['a','i','z','v','s','e','a','d','s','e','r','m','m','e','s','l']
l2 = ['a','t','r','l','s','e','a','d','s','5','r','g','w','e']
l3 = ['f','f','r','a','r']

def letter_check(word, letters) -> bool:
    # Store some booleans
    facts = []
    # Get some letter counts
    w = {letter: word.count(letter) for letter in ascii_lowercase if word.count(letter) != 0}
    l = {letter: letters.count(letter) for letter in ascii_lowercase if letters.count(letter) != 0}
    # Check if the letter counts in the list are sufficient
    for letter in word:
        try:
            # Build that boolean list
            if l[letter] >= w[letter]:
                facts.append(True)
            else:
                facts.append(False)
        # Ignore letters that aren't needed
        except KeyError:
            pass
    # Check the boolean list and give an answer
    return True if not False in facts and len(facts) == len(word) else False

print(letter_check(word, l1))