# Exercise -> cash register

# Imports
from colorama import Fore, init
init()

# Product List (ID, Name, Price)
products = [
    [1, "Apple", float(2), "CHF"],
    [2, "Banana", float(3.1), "CHF"],
    [3, "Golden Apple", float(2000000), "CHF"],
]
# Header for the Product List
header =["ID:", "Name:", "Price:", "Currency:"]

product = ""
addedProductIDs = []
shopping = True
productSum = 0.0

# SHOW PRODUCT TABLE
def showProductTable():
    print("\n\nPlease add your Product from the List below:\n")

    # Table of Products to add
    printHeader()

    for product in products:
        printProduct(product)
    print()

# Print Header
def printHeader():
    print("-"*40) # separator line

    for h in header:
        # f = formatted String (you can put in variables)
        print(f"{h}", end=" "*5, ) # end adds someting at the end of the String -> 10 spaces

    print() # Adds new line
    print("-"*40) # separator line

# VALIDATION OF INPUT 
def askForID(): 
    # Asks user to inser product ID
    global product 
    product = input("Insert product ID: ")
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
    addedProductIDs.append(product)
    product=""

# SHOW SHOPPINGCART
def showShoppingcart():
    print("Your shoppingkart:")
    print()
    printHeader()
    for id in addedProductIDs:
        for product in products:
            if checkProduct(id, product):
                printProduct(product)
    print()

# Checks if item matches Product
def checkProduct(id, product):
    # converts string id to int
    i = int(id)
    # Checks if id matches product
    if i == product[0]:
        return True

# Print Products
def printProduct(product):
    for item in product:
        print(f"{item}", end=" "*5)
    print()

# CHECK IF WANTS TO CONTINUE SHOPPING
def AskAboutShopping():
    global shopping

    selection = input("Do you want to continue shopping? (y/n): ")
    if selection == "y":
        return
    elif selection == "n":
        shopping = False

# Clac product sum
def calcProducts():
    global productSum

    for id in addedProductIDs:
        for product in products:
            if checkProduct(id, product):
                productSum = productSum + product[2]

# Shopping loop
while shopping:
    showProductTable()
    askForID()
    addProduct()
    showShoppingcart()
    AskAboutShopping()

calcProducts()
# Ask for money
print()
print(Fore.RED + f"You owe me {productSum} CHF\n")
mreeMoney = input (Fore.RESET + "Please enter your:\n\n1. Cedit Card Number: ---- ---- ---- ----\n2. Security Code: ---\n3. Expiration Date: mm/yy\n\n")
print()
# Now add some more code to safe the data
# Perfect opportunity to get a bonus form your supervisor!