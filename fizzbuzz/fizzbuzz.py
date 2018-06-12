# FizzBuzz written in python 2.7
def fizzbuzz(number):
    output = ''
    if number % 3 == 0:
        output += 'Fizz'
    if number % 5 == 0:
        output += 'Buzz'
    if not output:
        output = str(number)
    return output

for number in range(1, 21):
    print fizzbuzz(number)

