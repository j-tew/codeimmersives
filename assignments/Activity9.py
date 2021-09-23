# Write a function that prints all the values in a list
myList = ["stuff", 22, "other stuff", 13, "the rest of the stuff"]

def write_em_out(l):
    for i in l:
        print(i)

write_em_out(myList)

# Write a function that prints a string a specified number of times
num = 13

def do_this_many(x):
    for i in range(x):
        print("your name")

do_this_many(num)