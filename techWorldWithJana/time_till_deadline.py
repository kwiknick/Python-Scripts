from datetime import datetime

user_input = input("Enter your goal with a deadline separated by a colon\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadlineFormatted = datetime.strptime(deadline, "%d.%m.%Y")
todaysDate = datetime.today()
timeUntilDeadline = deadlineFormatted - todaysDate

# calculate how many days from now till the deadline
print(f"Dear user!  Time remaining for your goal: {goal} is {timeUntilDeadline.days} days")
