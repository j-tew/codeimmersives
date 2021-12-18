# Create a while loop that prints the 12 days of Christmas

# Dictionary for the items
items = {
    1: "A partridge in a pear tree",
    2: "Two turtle doves",
    3: "Three french hens",
    4: "Four calling birds",
    5: "Five gold rings",
    6: "Six geese a-laying",
    7: "Seven swans a-swimming",
    8: "Eight maids a-milking",
    9: "Nine ladies dancing",
    10: "Ten lords a-leaping",
    11: "Eleven pipers piping",
    12: "Twelve drummers drumming"
}
# Dictionary for the days
day_of_Christmas = {
    1: "First",
    2: "Second",
    3: "Third",
    4: "Fourth",
    5: "Fifth",
    6: "Sixth",
    7: "Seventh",
    8: "Eighth",
    9: "Ninth",
    10: "Tenth",
    11: "Eleventh",
    12: "Twelfth"
}
# While loop to print the lyrics
day = 1
while day <= 12:
    print(f"On the {day_of_Christmas[day]} day of Christmas, my true love gave to me\n{items[day]}\n")
    day += 1




# Create a while loop that prints the sum of integers from a list
nums = [1, 2, 3]
i = 0
total = 0
while i < len(nums):
    total += nums[i]
    i += 1
print(total)