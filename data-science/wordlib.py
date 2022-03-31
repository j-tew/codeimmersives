from string import ascii_letters
from random import sample, randint

class Word:
    '''A class object providing methods to operate on words.'''
    
    def __init__(self, word: str) -> None:
        # Get a list of vowels
        self.vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        # Get a list of consonants
        self.consonants = [l for l in list(ascii_letters) if l not in self.vowels]
        # Save the word
        self.word = word
        # Convert the letters to a dictionary to access indices
        self.dictionary = dict(zip(range(len(self.word)), self.word))

    def remove_vowels(self, replacement: str='_', replace: bool=False) -> str:
        '''Removes the vowels from the word. A replacement string can be passed,
        but replace=True must be passed also. The default replacement is an undercore.'''
        # Make a shallow copy of the letters
        word = dict(self.dictionary)
        # Find the indices of all the vowels and put them in a list
        locations = [i for i, l in word.items() if l in self.vowels]
        # Checking for keyword arg 'replace'
        if replace == True:
            # Iterate the indices of the vowels
            for i in locations:
                # Replace the letter
                word[i] = replacement
        else:
            # With no keyword arg
            for i in locations:
                # Remove the letter
                word[i] = ''
        # Convert the dictionary back to a string
        return ''.join(word.values())

    def remove_consonants(self, replacement: str = '_', replace: bool=False) -> str:
        '''Removes the consonants from the word. A replacement string can be passed,
        but replace=True must be passed also. The default replacement is an undercore.'''
        # Make a shallow copy of the letters
        word = dict(self.dictionary)
        # Find the indices of all the consonants and put them in a list
        locations = [i for i, l in word.items() if l in self.consonants]
        # Check for keyword arg 'replace'
        if replace == True:
            # Iterate the indices of the consonants
            for i in locations:
                # Replace the letter
                word[i] = replacement
        else:
            # With no keyword arg
            for i in locations:
                # Remove the letter
                word[i] = ''
        # Convert the dictionary back to a string
        return ''.join(word.values())

    def remove_fixed(self, step: int=1, replacement: str = '_', replace: bool=False) -> str:
        '''Removes a specified number of letters from the word.
        If no step is given, all the letters are rmeoved or replaced.
        A replacement string can be passed, but replace=True must be passed also.
        The default replacement is an undercore.'''
        # Make a shallow copy of the letters
        word = dict(self.dictionary)
        # Check for keyword arg 'replace'
        if replace == True:
            # Iterate the dictionary using the step
            for i in range(0, len(self.word), step):
                # Replace the indices based on the step (Spaces will be replaced if at the index)
                word[i] = replacement
        else:
            # With no keyword argument
            for i in range(0, len(self.word), step):
                # Remove the letter
                word[i] = ''
        # Convert the dictionary back to a string
        return ''.join(word.values())

    def random_remove(self, max_count: int=0, replacement: str='_', replace: bool=False) -> tuple:
        '''Removes a random number of letters up to the number specified in the arguments
        and returns a tuple with the new word and the number of letters changed.
        If no max_count is given, no letters get changed.
        A replacement string can be passed, but replace=True must be passed also.
        The default replacement is an undercore.'''
        # Make a shallow copy of the letters
        word = dict(self.dictionary)
        # Set the limit for 'max_count'
        limit = len(self.word) - 1
        # Ensure 'max_count' isn't larger than the length of the string
        max_count = limit if max_count > limit else max_count
        # Select a number of random indices based on a random number between 0 and 'max_count'
        randoms = sample(range(limit + 1), randint(0, max_count))
        # Check for keyword arg 'replace'
        if replace == True:
            # Iterate the indices based on the random selections
            for i in randoms:
                # Replace the letter (Spaces will be replaced if at the index)
                word[i] = replacement
        else:
            # With no keyword argument
            for i in randoms:
                # Remove the letter
                word[i] = ''
        # Convert the dictionary back to a string
        return ''.join(word.values()), len(randoms)

    def __str__(self) -> str:
        '''Print the number of vowels and consonants in the word.'''
        # Count the number of vowels
        vowels = len([l for l in self.word if l in self.vowels])
        # Count the number of consonants
        consonants = len([l for l in self.word if l in self.consonants])
        return f'"{self.word}" has {vowels} vowels and {consonants} consonants.'
