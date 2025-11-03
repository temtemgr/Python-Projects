# cash register

import json

# header for the product list
header =["ID:", "Name:", "Price:", "Currency:"]

# load data
products_JSON = open("Cashregister\Products.json")
products = json.load(products_JSON)

product = ""
added_product_ids = []
shopping = True
product_sum = 0

# show product table
def show_product_table():
    print("\n\nPlease add your Product from the List below:\n")

    # Table of Products to add
    print_header()

    for product in products:
        print_product(product)

# print header
def print_header():
    print("-"*40) # separator line

    for h in header:
        # f = formatted String (you can put in variables)
        print(f"{h}", end=" "*5, ) # end adds someting at the end of the String -> 10 spaces
    print()
    print("-"*40) # separator line

# print products
def print_product(product):
    print(f"{product["id"]}  {product["name"]}  {product["price"]}  {product["currency"]}\n")

# asks for product id
def ask_for_id(): 
    global product 
    product = input("Insert product ID: ")
    validate_product(product)
    print()

# validation of input
def validate_product(new_product):

    for product in products:
    # valitade if whole number (digit)
        if new_product.isdigit():
            # Validates if Product exists    
            if product["id"] == int(new_product):
                return
    print("This is not a product ID or a whole number... Try again\n")
    ask_for_id()

# shows shoppingcart
def show_shoppingcart():
    print("Your shoppingkart:\n")
    print_header()
    loop_over_added_products(print_product)

# loops over added products and passes
def loop_over_added_products(functionToRun):
    for id in added_product_ids:
        for product in products:
            if int(id) == product["id"]:
                functionToRun(product)

# check if they want to continue shopping
def ask_to_continue():
    global shopping

    selection = input("Do you want to continue shopping? (y/n): ")
    if selection == "y":
        return
    elif selection == "n":
        shopping = False
    else:
        ask_to_continue()

# claculates product sum
def calc_product_sum(product):
    global product_sum
    product_sum = product_sum + product["price"]

# shopping loop

while shopping:
    show_product_table()
    ask_for_id()
    added_product_ids.append(int(product))
    product=""
    show_shoppingcart()
    ask_to_continue()

loop_over_added_products(calc_product_sum)

# Ask for money
print("\n\n")
print(f"Product Sum: {product_sum} CHF\n")
card_details = input ("Please enter your:\n\n1. Cedit Card Number: ---- ---- ---- ----\n2. Security Code: ---\n3. Expiration Date: mm/yy\n\n")