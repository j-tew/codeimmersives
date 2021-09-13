answer = input("Binary or Decimal? Please enter (b/d):\n")

# Function to convert binary numbers to decimal
def binConv(x):
    binary = x[::-1]
    total = 0
    bit = 1
    for i in binary:
        if i == "1":
            total += bit
            bit *= 2
        elif i == "0":
            total += 0
            bit *= 2
    return total

# Function to convert decimal numbers to binary
# Fix int() functions later (when controlling input)
def decConv(x):
    bits = ""
    x = int(x)
    while x >= 1:
        bits += str(x % 2)
        x = int(x / 2)
    binary = bits[::-1]
    return binary

if answer == "b":
    binNum = input("Please enter a binary number:\n")
    # Add code for binary to decimal conversion
    print(binConv(binNum))
elif answer == "d":
    decNum = input("Please enter a decimal number:\n")
    # Add code for decimal to binary conversion
    print(decConv(decNum))
else:
    print("Invalid Input")
