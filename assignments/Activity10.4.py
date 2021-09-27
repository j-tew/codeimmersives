def palindrome(x):
    if x == x[::-1]:
        return True
    else:
        return False

pword = "racecar"
word = "gangsta"

print(f"Is \"{word}\" a palindrome?\n{palindrome(word)}\n")
print(f"Is \"{pword}\" a palindrome?\n{palindrome(pword)}\n")
