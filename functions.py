# Homework problem #1

from IPython.display import clear_output

def inventory_mgmt():
    inventory = []
    temp_add = []
    while True:
        # Step 4
        main_input = input("Show/Add/Delete or Quit: ").lower()
        clear_output
        # if input = show, print dictionary
        if main_input == 'show':
            print(inventory)
        elif main_input == 'add':
            adding = input("Please type what you would like to add to the inventory: ").lower()
            inventory.insert(0,adding)
            print(inventory)
        elif main_input == 'delete':
            deleting = input("Please type what item you would like to delete from inventory: ").lower()
            inventory.remove(deleting)
            print(inventory)
        elif main_input == 'quit':
            print("Thank you, the following items are included in your shopping cart:  ")
            for item in inventory:
                print(item)
            break
# calling function
inventory_mgmt()

#Question 2

def area_of_house(length, width):
    return length * width
    
print(area_of_house(30,50))

#Question #3

import math

def circumfrence(radius):
    print("The circumfrence of the circle is: ")   
    return radius * 2 * math.pi

print(circumfrence(5))

