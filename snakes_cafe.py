global continue_order
menu_dict = {
    "Wings": 0,
    "Cookies": 0,
    "Spring Rolls": 0,
    "Salmon": 0,
    "Steak": 0,
    "Meat Tornado": 0,
    "A Literal Garden": 0,
    "Ice Cream": 0,
    "Cake": 0,
    "Pie": 0,
    "Coffee": 0,
    "Tea": 0,
    "Unicorn Tears": 0
}
def new_order():
    for i in menu_dict:
        menu_dict[i] = 0
def display_menu():
    new_order()
    print(("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**                                  **
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
"""))

def confirm_order():

    print("""
  **************************************
  **        Your order is below.      **
  **     Thank you for your order.    **
  **                                  **
  ** To quit at any time, type "quit" **
  **************************************
  """)
    print(menu_dict)
    print("Please enter 'y' for yes to place another order.  Type 'quit' to exit.")
    reorder = input("> ")
    while reorder != "y":
        confirm_order()
        if reorder == "quit":
            continue_order = False
            break
    display_menu()
    place_order()

def place_order():
    ask_order = input("> ")
    while ask_order != "quit":
        if ask_order in menu_dict:
            menu_dict[ask_order] += 1
            break
        else:
            print("The item you selected is not available.  Please select an item again")
            place_order()
    if menu_dict[ask_order] == 1:
        print(f"** {menu_dict[ask_order]} order of {ask_order} is now on your order **")
    else:
        print(f"** {menu_dict[ask_order]} orders of {ask_order} are now on your order **")


    continue_order = True
    while continue_order:
        print("Order another item? Please enter 'y' for yes or 'n' for no")
        choice = input("> ")
        if choice == "y":
            print("""
      ****************************************
      ** What else would you like to order? **
      ****************************************
      **   type 'quit' to cancel ordering   **
      """)
            place_order()
        elif choice == "n":
            continue_order = False
            confirm_order()
        elif choice == "quit":
            break
        else:
            print(f"Invalid entry. Please enter 'y' for yes or 'n' for no.")

if __name__ == "__main__":
    display_menu()
    new_order()
    place_order()