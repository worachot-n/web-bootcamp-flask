name = input("Enter your name: ")
print(name)

size_input = input("How big is your house (in square feet): ")
squar_feet = int(size_input)
square_metres = squar_feet / 10.8
print(f"{squar_feet} square feet is {square_metres:.2f} square metres.")
