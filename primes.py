"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

import math

def primes(number_of_primes):
    list = []

    if number_of_primes < 1:
        raise ValueError
    
        return list

    list.append(2)
    """ We have just added one prime so start i from 1 """
    i = 1
    
    value = 1
    
    while(i < number_of_primes):
        found = False
        
        while(found != True):
            """ Value starts at 1. += 2 to skip all multiples of 2 as a
                simple optimisation """
            value += 2

            found = True

            """ Check if value has no divisors apart from 1 and itself """
            for j in range(2, value):
                if(value % j == 0):
                    """ It has a divisor so found is False """
                    found = False
                    break;
            if found == True:
                print("Found is true for value: " + str(value))

        
        list.append(value)
        i += 1

    return list
