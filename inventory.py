
#========The beginning of the class==========
class Shoe:
    '''Shoe class for storing stock information. the ___str___ prints each object
    in a readable format'''
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        output =  f"----- {self.product} -----\n"
        output += f"Country: {self.country}\n"
        output += f"Code: {self.code}\n"
        output += f"Cost: £{self.cost}\n"
        output += f"Quantity: {self.quantity}\n"
        output += "----------------------\n"

        return output


#============= Shoe list =========== #

shoe_list = []
#========== Functions outside the class ============== #
def read_shoes_data():
    '''Captures the shoes from the txt file and casts them as Shoe objects
    into the shoe_list list.'''

    file = open("inventory.txt", "r")
    shoes = file.readlines()

    for row in shoes[1:]:
        row = row.split(",")
        shoe = Shoe(row[0],row[1],row[2],row[3],row[4])
        shoe_list.append(shoe)

    file.close()

def capture_shoes():
    '''Adds a new Shoe object to the shoe_list list'''
    country = input("Country: ")
    code = input("Code: ")
    product = input("Product: ")
    cost = input("Cost: ")
    quantity = input("Quantity: ")

    new_shoe = Shoe(country,code,product,cost,quantity)
    shoe_list.append(new_shoe)
    print("Shoe added to stock:")
    print(new_shoe)

def view_all():
    pass
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''
    for item in shoe_list:
        print(item)

def re_stock():
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoe that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
    min = shoe_list[0].quantity
    min_obj = shoe_list[0]

    for ind, obj in enumerate(shoe_list):

        if obj.quantity < min:
            min = obj.quantity
            min_obj = obj
            index = ind
    print(f"The item the least in stock is {min_obj.product}")
    while True:
        restock = input("Would you like to re-stock this item? y/n: ").lower()
        if restock == "n":
            break
            return
        elif restock == "y":
            while True:
                try:
                    amount = int(input("How much is now in stock? "))
                    shoe_list[index].quantity = amount
                    break
                except:
                    print("Please enter a number")
            break
        else:
            pass

def search_shoe():
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
    id = input("Enter the shoe ID#: ")

    for obj in shoe_list:
        if obj.code == id:
            print(obj)

def value_per_item():
    '''Iterates through stock and shows the value per item (cost * quantity'''
    for obj in shoe_list:
        value = int(obj.cost) * int(obj.quantity)
        print(f"{obj.product}\nValue: {value}\n")

def highest_qty():
    ''' Finds the item with the most stock and prints to console'''
    highest_quantity = 0
    highest_product = ""
    for obj in shoe_list:
        quantity = int(obj.quantity)
        if quantity > highest_quantity:
            highest_quantity = quantity
            highest_product = obj.product
    print(f"\nHighest quantity:\n{highest_product}: {highest_quantity}\n")

# ========== Main Menu ============= #
# ASCII Shoe to print to console on start up.

shoe_art = '''
        ________
     __(_____  <|
    (____ / <| <|
    (___ /  <| L`-------.
    (__ /   L`--------.  /
    /  `.    ^^^^^ |   \  |
   |     \---------'    |/
   |______|____________/]
   [_____|`-.__________]
   '''

# Menu Template
menu  = "---------- [Inventory] ----------\n"
menu += "1: View full inventory.\n"
menu += "2: Add new shoe to stock\n"
menu += "3: Re-stock lowest item\n"
menu += "4: Search for a shoe by code\n"
menu += "5: See Value per item\n"
menu += "6: Show product with highest stock\n"
menu += "7: Exit"

# Print ASCII Shoe
print(shoe_art)

# Read data in from txt file
read_shoes_data()

# While loop for menu.
while True:
    print(menu)
    # Ensure datd entered is an int and a valid choice with try except.
    try:
        choice = int(input("Select a number from the menu: "))

        # View all stock use class ___str___ print for clarity
        if choice == 1:
            view_all()

        # Add new shoe to list
        elif choice == 2:
            capture_shoes()

        # Re-stock lowest stock item
        elif choice == 3:
            re_stock()

        # Search for shoe by SKU code
        elif choice == 4:
            search_shoe()

        # Disply the value per item for all shoes
        elif choice == 5:
            value_per_item()

        # Show the shoe with the highest quantity of stock
        elif choice == 6:
            highest_qty()

        # Exit
        elif choice == 7:
            print("Goodbye.")
            break
    except:
        print("Please enter a valid number")

