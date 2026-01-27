# Question 2: Shopping cart(Lists- Searching and Removal)
cart = ["apple","banana","milk","bread","apple","eggs"]
print("Number of apples", cart.count,"apple")
print("position of milk", cart.index("milk"))
cart.remove("apple")
print("Removal items using pop:", cart.pop())
print("Is banana in the cart?","banana" in cart)
print("final cart:",cart)