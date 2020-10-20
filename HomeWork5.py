"""
From the numbers from 1 to 100, control for multiples of three and print "Fizz" instead, for the multiples of five print "Buzz".
For numbers which are multiples of both three and five print "FizzBuzz". Instead of only printing "fizz", "buzz", and "fizzbuzz",
add a fourth print category: "prime", other must be printed as numbers without category.
"""

from math import floor, sqrt

def _is_prime(num):
    """Controlling if the number is prime"""
    for test in range(2, floor(sqrt(num)) + 1):
        if num % test == 0:
            return False

    # 1 is not considered prime
    return num > 1

"""
Print Fizz Buzz FizzBuzz prime or the number
"""
for num in range(1, 101):
    output = ''

    if _is_prime(num):
        output = 'Prime'
    else:
        if num % 3 == 0:
            output += 'Fizz'
        if num % 5 == 0:
            output += 'Buzz'

    # print output results
    print(output if len(output) else num)