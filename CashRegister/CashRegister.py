# Exercise Week 2 -> cash register

# Product List (ID, Name, Price)
products = [
    [1, "Apple", float(2)],
    [2, "Banana", float(3.1)],
    [3, "Golden Apple", float(2000000)],
]
# Header for the Product List
header =["ID:", "Name:", "Price:"]

product = ""
addedProducts = []
shopping = True

# SHOW PRODUCT TABLE
def showProductTable():
    print("\n\nPlease add your Product from the List below:\n")

    # Table of Products to add
    print("-"*40) # separator line

    for h in header:
        # f = formatted String (you can put in variables)
        print(f"{h}", end=" "*10, ) # end adds someting at the end of the String -> 10 spaces

    print() # Adds new line
    print("-"*40) # separator line

    for product in products:
        for item in product:
            print(f"{item}", end=" "*5)
        print()
    print()

# VALIDATION OF INPUT 
def askForID(): 
    # Asks user to inser product ID
    global product 
    product = input("Insert product ID:")
    print()

    # Valitade if digit (whole number)
    if product.isdigit():
            newProduct = int(product)
            validateProduct(newProduct)
    else:
        print("This is not whole a number... Try again\n")
        askForID()

# Validates if Product exists
def validateProduct(newProduct):
    for product in products:
        if product[0] == newProduct:
            return
    print("This is not a product ID... Try again\n")
    askForID()

# ADDS PRODUCT
def addProduct():
    global product
    addedProducts.append(product)
    product=""

# SHOW SHOPPINGCART
def showShoppincart():
    print()

while shopping:
    showProductTable()
    askForID()
    addProduct()

