# EXERCISE 2: A shopping cart program.

item_name = input("What stuff do you got? ")
price = float(input("How much is it? "))
quantity = int(input("How many? "))

total = price * quantity

print(f"{item_name} cost ${total} sir.")