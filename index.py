# Imported the random module onto my python script.
import random

# Created a function called FizzBuzz.
# The function takes in an argument of num, which is a number.
# The first conditional statement uses a Modulo operator, which will determine if an integer is divisible by another integer.
# In the first conditional statement, if the num argument is divisible by both 3 and 5, the function will print out 'FizzBuzz' to the terminal.
# Otherwise, the function will run the next conditional statement.
# In the second conditional statement, if the num argument is divisible by 3, the function will print out 'Fizz' onto the terminal.
# Otherwise, if the num argument is divisible by 5, the function will print out 'Buzz' onto the terminal.
# Otherwise, the function will print out 'Input is not an integer, or the integer is not divisible by 3 or 5.' onto the terminal.


def FizzBuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    else:
        if num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print("Input is not an integer, or the integer is not divisible by 3 or 5.")


# Here the variable n equals a built in function called 'random' that will generate a random number between the numbers of 0 and 15.
n = random.randint(0, 15)

# The result n will be printed onto the console.
# The function FizzBuzz will be called and executed.
print(n)
FizzBuzz(n)
