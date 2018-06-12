#bubblesort.py
#simple sorting algorithm

from random import shuffle

def get_list():
    """Takes data from the user and creates a list."""
    print("Enter your numbers.\nLeave a space between each one.")
    my_list = [int(number) for number in raw_input("Enter integers: ").split()]
    return my_list
#main
print("Welcome to Bubble Sort.")
unsorted = []

#setting up a simple menu
ans = None
while ans != 'q':
    print(
        """You have 3 options:
        1: Use numbers 1-20 shuffled.
        2: Input your own values.
        q: Quit.""")
    ans = raw_input("\nWhat do you want to do? ")
    if str(ans) == 'q':
        continue
    elif int(ans) == 1:
        #initialise the list
        unsorted = list(range(20))
        #shuffle the numbers
        shuffle(unsorted)
        print("Randomised list created")
    elif int(ans) == 2:
        unsorted = get_list()
        #shuffle the numbers
        shuffle(unsorted)
        print("You gave me:")
    else:
        print("Unrecognised choice.")
        continue
    print(unsorted)

