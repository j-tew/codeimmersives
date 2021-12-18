# Finding the greatest of 3 numbers
nums = [22, 2, 13]
greatest = nums[0]
for num in nums:
    if num > greatest:
        greatest = num
print(f"{greatest} is the greatest number of the three numbers.\n")
# Traffic Light
validChoices = ("green", "yellow", "red")
light = {"green": "Go!", "yellow": "Slow Down!", "red": "Stop!"}
color = input(f"You see a traffic light ahead. What color is it?\nPlease enter red, yellow, or green:\n")
# Input validation and accepting capital letters
corrected = color.lower()
if corrected in validChoices:
    print(light[corrected])
else:
    print(f"That is an invalid slection.")