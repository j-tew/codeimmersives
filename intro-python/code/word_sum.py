def word_sum(wrd):
    letters = [ord(l) for l in wrd]
    return sum(letters)

words = ['Love','Python','Dictionary','List','Tuple','Set','Ternary']
sums = [(word, word_sum(word)) for word in words]

print(sums)