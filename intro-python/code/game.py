# Playing with Classes

class Pencil:
    isSharpened = False
    hasEraser = True

    def __init__(self, color):
        self.color = color

    def sharpen(self):
        self.isSharpened = True
        print("Sharpening...")

p1 = Pencil("Green")

print(f"We have a pencil and it is {p1.color}.\n")
print(f"Our Pencil is Sharpened: {p1.isSharpened}")
p1.sharpen()
print(f"Our Pencil is Sharpened: {p1.isSharpened}")