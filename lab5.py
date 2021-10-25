# Programmers: Aidan, Nicol
# Course: CS151, Dr. Rajeev
# Date: 10/21/2021
# Lab Number: 5
# Program Inputs: floor type and floor width and length
# Program Outputs: floor price and sqft

# Problem Your friends just bought a new five room house and need your help to know how much it will cost to re-do
# the floors. Write a program that, given the dimensions of each of the five rooms and the desired type of flooring,
# outputs the cost of each room as well as the total cost. Hardwood costs $1.39/sqft, carpet costs $3.99/sqft, and
# tile costs $4.99/sqft.

# Input Validation: Your program must work regardless of the case the floor option is typed in and any blank spaces
# surrounding it; If an invalid option is given, inform the user it was invalid and that you will be skipping that
# room (treat the cost as zero).

# Round: Use the round function to round your output to two decimal places.

# Function decomposition Your program should have a function for each of the following tasks:


# Given a string representing a floor type, determine if it is a valid option.

# Given a string representing a valid floor type, return the cost per square foot of that floor type.

# Given a valid length and width in feet and a valid floor type, determine the cost of a single
# room of those dimensions for the given floor type.

# Process a single room, including asking the user to input values for room dimensions and floor type.

# After gathering the inputs form the user, this function should call one of the other functions to compute the values.

# A main function to drive the program.

def valid(message):
    if message == "hardwood" or message == "carpet" or message == "tile":
        return True
    else:
        return False

def dimensions(length, width, message):
    if length > 0 and width > 0:
        total_cost = setPrice(message) * length * width
    else:
        total_cost = 0
    return total_cost

def setPrice(message):
    if message == "hardwood":
        price = 1.39
    elif message == "carpet":
        price = 3.99
    elif message == "tile":
        price = 4.99
    return price



def cost_room():
    message = input("What type of floor: ")
    message = message.lower().strip()
    floor_validity = valid(message)
    if floor_validity == True:
        length = float(input("What's the length of the room in feet: "))
        width = float(input("What's the width of the room in feet: "))
        floor_cost = dimensions(length, width, message)
        if floor_cost == 0:
            print("Skipping this room because of invalid dimension.")
        else:
            print("This room costs $", round(floor_cost, 2))
    else:
        print("Skipping this room because of invalid floor type.")
        floor_cost = 0
    return floor_cost

def main():
    rooms = 1
    total = 0
    while rooms < 6:
        print("Room", rooms)
        room_cost = cost_room()
        total += room_cost
        rooms += 1
    print("Total of all rooms in house is $", round(total, 2))

main()