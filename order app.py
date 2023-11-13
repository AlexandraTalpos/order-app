RESTAURANT_NAME = "Angry Bite"

# Using a nested dictionary for the menu
menu = {
    "sku1": {
        "name": "Hamburger",
        "price": 6.49
    },
    "sku2": {
        "name": "Cheeseburger",
        "price": 7.80
    },
    "sku3": {
        "name": "Milkshake",
        "price": 4.99
    },
    "sku4": {
        "name": "Fries",
        "price": 2.45
    },
    "sku5": {
        "name": "Sandwich",
        "price": 5.90
    },
    "sku6": {
        "name": "Ice Cream",
        "price": 1.49
    },
    "sku7": {
        "name": "Drink",
        "price": 4.10
    },
    "sku8": {
        "name": "Cookie",
        "price": 3.15
    },
    "sku9": {
        "name": "Doughnut",
        "price": 2.45
    },
    "sku10": {
        "name": "Sauce",
        "price": 0.65
        }
}
app_actions = {
    "1": "Add a new menu item to cart",
    "2": "Remove an item from the cart",
    "3": "Modify a cart item's quantity",
    "4": "View cart",
    "5": "Checkout",
    "6": "Exit"
}
# We can use a global constant here since the sale tax will remain unchanged
SALES_TAX_RATE = 0.07
cart = {}

def display_menu():
    """Displays all menu item SKUs, names, and prices."""
    # Display a header message
    print("\n****Menu****\n")
    for sku in menu:
        # Slice the leading 'sku' string to retrieve the number portion
        parsed_sku = sku[3:]
        item = menu[sku]['name']
        price = menu[sku]['price']
        print("(" + parsed_sku + ")" + " " + item + ": $" + str(price))
    print("\n")

def add_to_cart(sku, quantity=1):
    """
    Add an item and its quantity to the cart.
    
    :param string sku: The input SKU number being ordered.
    :param int quantity: The input quantity being ordered.
    """
    if sku in menu:
        if sku in cart:
            cart[sku] += quantity
        else:
            cart[sku] = quantity
        print("Added ", quantity, " of ", menu[sku]['name'], " to the cart.")
    else:
        print("I'm sorry. The menu number", sku, "that you entered is not on the menu.")


def remove_from_cart(sku):
    """
    Remove an item from the cart.
    
    :param string sku: The input SKU number to remove from the cart.
    """
    if sku in cart:
        removed_val = cart.pop(sku)
        print(f"Removed", removed_val['name'], "from the cart.")
    else:
        print("I'm sorry.", removed_val['name'], "is not currently in the cart.")

def modify_cart(sku, quantity):
    """
    Modify an item's quantity in the cart.
    
    :param string sku: The input SKU number being modified.
    :param int quantity: The input new quantity to use for the SKU.
    """
    if sku in cart:
        if quantity > 0:
            cart[sku] = quantity
            print("Modified", menu[sku]['name'], "quantity to ", quantity, " in the cart.")
        else:
            # Call the previously defined function to remove a SKU from the cart
            remove_from_cart(sku)
    else:
        print(f"I'm sorry.", menu[sku]['name'], "is not currently in the cart.")


def view_cart():
    """
    Display the menu item names and quanitites inside 
    the cart.
    """
    # Display a header message
    print("\n****Cart Contents****\n")
    subtotal = 0
    for sku in cart:
        if sku in menu:
            quantity  = cart[sku]
            subtotal += menu[sku]["price"] * quantity
            print(quantity, " x ", menu[sku]["name"])
    tax = subtotal * SALES_TAX_RATE
    total = subtotal + tax
    print("Total: $", round(total, 2))
    print("\n")

def checkout():
    """Display the subtotal information for the user to checkout"""
    # Display a header message
    print("\n****Checkout****\n")
    # Call the previously defined function to view the cart contents
    view_cart()
    print("Thank you for your order! See you next time!")
    print("\n")


def get_sku_and_quantity(sku_prompt, quantity_prompt=None):
    """
    Get input from the user.
    
    :param string sku_prompt: A string representing the prompt to display to the user before they enter the SKU number.
    :param string quantity_prompt: A string representing the prompt to display to the user before they enter the quantity.
        This defaults to None for cases where quanitity input is not needed.
        
    :returns: The full sku# value and the quantity (in certain cases)
    """
    # Use the SKU prompt to get input from the user
    item_sku = input(sku_prompt)
    # String concatenate "sku" to the beginning of the entered SKU number
    item_sku = "sku" + item_sku
    # If the quantity prompt is provided, we should get input from the user 
    if quantity_prompt:
        # Use the quantity prompt to get input from the user
        quantity = input(quantity_prompt)
        # If the user typed a non-digit value, default quantity to 1
        if not quantity.isdigit():
            quantity = 1
        quantity = int(quantity)

        return item_sku, quantity
    # Quantity prompt is None meaning we do not need to get input for quantity
    else:
        return item_sku


def order_loop():
    """Loop ordering actions until checkout or exit"""
    # Display a welcome message to the user
    print("Welcome to the " + RESTAURANT_NAME + "!")
    # Set the conditional boolean variable that will be used to determine if the while loop
    # continues running or whether it should terminate
    ordering = True
    while ordering:
        # Display the app ordering actions
        print("\n****Ordering Actions****\n")
        for number in app_actions:
            description = app_actions[number]
            print("(" + number + ")", description)
        
        response = input("Please enter the number of the action you want to take: ")
        if response == "1":
            # User wants to order a menu item. Prompt them for SKU and quantity.
            display_menu()
            sku_prompt = "Please enter the SKU number for the menu item you want to order: "
            quantity_prompt = "Please enter the quantity you want to order [default is 1]: "
            ordered_sku, quantity = get_sku_and_quantity(sku_prompt, quantity_prompt)
            add_to_cart(ordered_sku, quantity)
        elif response == "2":
            # User wants to remove an item from the cart. Prompt them for SKU only.
            display_menu()
            sku_prompt = "Please enter the SKU number for the menu item you want to remove: "
            item_sku = get_sku_and_quantity(sku_prompt)
            remove_from_cart(item_sku)
        elif response == "3":
            # User wants to modify an item quantity in the cart. Prompt them for SKU and quantity.
            display_menu()
            sku_prompt = "Please enter the SKU number for the menu item you want to modify: "
            quantity_prompt = "Please enter the quantity you want to change to [default is 1]: "
            item_sku, quantity = get_sku_and_quantity(sku_prompt, quantity_prompt)
            modify_cart(item_sku, quantity)
        elif response == "4":
            # User wants to view the current cart contents. No user input needed.
            view_cart()
        elif response == "5":
            # User wants to checkout. No user input needed. Terminate the while loop after displaying.
            checkout()
            ordering = False
        elif response == "6":
            # User wants to exit before ordering. No user input needed. Terminate the while loop.
            print("Goodbye!")
            ordering = False
        else:
            # User has entered an invalid action number. Display a message.
            print("You have entered an invalid action number. Please try again.")



order_loop()
