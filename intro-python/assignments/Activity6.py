car = {"brand": "Ford", "model": "Mustang", "year": 1964}
# .get()	Returns the value of the specified key
model = car.get("model")
print(f"Model: {model}\n")

# .copy()	Returns a copy of the dictionary
car0 = car.copy()
print(f"This is a copy of the dictionary:\n{car0}\n")

# .clear()	Removes all the elements from the dictionary
car0.clear()
print(f"This is the cleared dictionary:\n{car0}\n")

# .items()	Returns a list containing a tuple for each key value pair
tuples = car.items()
print(f"This is a LIST of TUPLES containing key:value pairs in the dictionary:\n{tuples}\n")

# .values()	Returns a list of all the values in the dictionary
values = car.values()
print(f"This is a LIST of VALUES in the dictionary:\n{values}\n")

# .keys()	Returns a list containing the dictionary's keys
keys = car.keys()
print(f"This is a LIST of KEYS in the dictionary:\n{keys}\n")

# .update()	Updates the dictionary with the specified key-value pairs
car.update({"color": "Green"})
print(f"This is the updated dictionary:\n{car}")




