#bubblesort.py
#simple sorting algorithm

from random import shuffle

def get_list():
    """Takes data from the user and creates a list."""
    err = True
    print("Enter your numbers.\nLeave a space between each one.")
    while err == True:
        err = False
        temp = input("Data:")
        my_list = temp.split()
        for item in my_list:
            try:
                item = float(item)
            except:
                print("Try again. Only numbers and spaces please.")
                err = True
                break
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
    ans = input("\nWhat do you want to do?")
    if ans == 'q':
        continue
    elif ans == '1':
        #initialise the list
        unsorted = list(range(20))
        #shuffle the numbers
        shuffle(unsorted)
        print("Randomised list created")
    elif ans == '2':
        unsorted = get_list()
        print("You gave me:")
    else:
        print("Unrecognised choice.")
        continue
    print(unsorted)


                                                             
