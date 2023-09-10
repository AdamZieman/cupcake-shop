# cupcake_shop.py
# This program follows the IPO (input, process, output) technique and imitates a cash register and a receipt.
# A user inputs the quantity of items that are purchased and outputs a sale of reciept with ASCII art.

# Course: CSCI 130 (Introduction to Programming)
# Assignment: 10

# Author: Adam Zieman
# Date: May 9, 2021

# printHeading()
# This function prints a heading and description of the program
def printHeading():
    print("Welcome to the Cupcake Shoppe!")
    print("As a small shop, orders per customer are limited:")
    print("Each customer can order up to 3 cupcakes")
    print("and up to 6 cups of coffee.\n")
    print("You will be asked for number of cups of coffee first,")
    print("then number of cupcakes.")
    print("Each cup of coffee costs $2 and each cupcake $1.75.")
    print("Your bill will be printed at the end.")
    print("#####################################################")


# getCount(item, maxToOrder)
# Asks the user to input a quantity of an item, inclusively between 0 and a max order size.
def getCount(item, maxToOrder):
    # User inputs the quantity of an item to purchase
    print("How many " + item + " do you wish to order? ", end="")
    order = int(input())

    # Checks the order size
    if order < 0: # if order size is less than 0, set it to 0
        print("Sorry, you cannot order a negative amount!")
        print("We will assume 0.")
        order = 0
    elif order > maxToOrder: # if order size is greater than the max order size, set it to the max order size
        print("Sorry, you can only order up to " + str(maxToOrder) + ".")
        print("We will prepare " + str(maxToOrder) + " for you.")
        order = maxToOrder

    return order # Returns the quantity of an ordered item


# calculateBill(coffees,cupcakes)
# Outputs the reciept of the sale with the quantity of items purchased,
# calculates and prints the total sale price, and
# ASCII art to represent the items purchased.
def calculateBill(coffees,cupcakes):
    print("Your order:")

    # Checks the amount of coffee purchased
    if coffees > 0: # If coffee was purchased, print the quantity purchased
        print(coffees, end="")

        # Prints the singular or plural version of 'coffee' based on the quantity purchased
        if coffees == 1:
            print(" coffee")
        else:
            print(" coffees")
            
        # Calls the drawCoffee() function for the quantity of coffees purchased
        for coffeeRepeat in range(coffees):
            drawCoffee()

    print("----------------") # Thin section seperator line
    
    # Checks the amount of cupcakes purchased
    if cupcakes > 0: # If cupcakes were purchased, print the quantity purchased
        print(cupcakes, end="")
        
        # Prints the singular or plural version of 'cupcake' based on the quantity purchased
        if cupcakes == 1:
            print(" cupcake")
        else:
            print(" cupcakes")
        
        # Calls the drawCupcake() function for the quantity of cupcakes purchased
        for cupcakeRepeat in range(cupcakes):
            drawCupcake()

    print("=========================") # Thick section seperator line

    # Calculate and prints the total sale price
    # total = [(price of ordered coffees) + (price of ordered cupcakes)] * (price after sales tax)
    total = round(((coffees * 2) + (cupcakes * 1.75)) * 1.055, 2)
    print("Your total is $", total, sep="")

    print("Enjoy your treats!") # Prints a farewell message


# drawCoffee()
# Draws an ASCII art of a coffee mug
def drawCoffee():
    print(" .-'---------|")
    print("( C *********|")
    print(" '-.*********|")
    print("   '_________'")
    print("    '-------'")


# drawCupcake()
# Draws an ASCII art of a frosted cupcake
def drawCupcake():
    print("   .--@@@--._")
    print("  ^-' *~-'@ ^.")
    print(" @@ . @ . ~ @")
    print(" \ ~  ^  @ @_/")
    print("[***-*-*-*-***]")
    print(" \| | | | | |/")
    print("  \ | | | | /")
    print("   ---===---")


# main()
def main():
    printHeading() # Calls the printHeading function to print a header and description of the program

    # Calls the getCount() function to store the amount of coffees and cupcakes purchased with a hardcoded max purchase quantity.
    numCoffees = getCount("cups of coffee", 6)
    numCupcakes = getCount("cupcakes", 3)    

    print("=====================================") # Thick line seperator
    calculateBill(numCoffees, numCupcakes) # Calls the calculateBill() function to calculate and print the receipt
    
main() # Calls the main() function
