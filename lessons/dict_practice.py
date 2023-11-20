"""Dictionary practice from lecture."""

# create a new dictionary

ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}
print("Create my dictionary:")
print(ice_cream)

# adding a key,value pair to a dictionary
ice_cream["mint"] = 3
print("Add mint to my dictionary")
print(ice_cream)

# removing elements from my dictionary
ice_cream.pop("mint")
print("Removed mint:")
print(ice_cream)

# access a value
print("How many orders of chocolate there are:")
print(ice_cream["chocolate"])

# modify using subscription notation
ice_cream["vanilla"] = 10
print("Update number of orders of vanilla to 10:")
print(ice_cream)

# length of dictionary (how many key-value pairs there are)
print(f"There are {len(ice_cream)} flavors of ice cream")

# check if key is in dictionary
print("Are mint and chocolate in the dictionary?")
print("mint" and "chocolate" in ice_cream)
print("Are there any orders of mint?")

if "mint" in ice_cream:
    print(ice_cream["mint"])
else: 
    print("no orders of mint")

# using for loops to iterate over keys by default
# the "'key' can be anything, such as 'flavor'"
for flavor in ice_cream:
    print(f"{flavor} has {ice_cream[flavor]} orders.")