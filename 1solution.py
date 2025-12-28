#!/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    x = number * -1
    y = x % 10
    print(y)
else:
    y = number % 10
    print(y)

print(f'Last number of {number} is {y}')
if y > 5 :
    print("and is greater than 5")
elif y == 0 :
    print("and is 0")
elif y < 6 and number != 0:
    print("and is less than 6 and is not 0")
