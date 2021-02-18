#################################################################################
#################################################################################
#################################################################################

# This file is to know if a number is a prime number




#################################################################################
import math
import random

def is_prime(number):
    if number < 1:
        pass
    else:
        for i in range(2, int(math.sqrt(number))):
            if number % i == 0:
                return False
                break
    return True







if __name__ == '__main__':
    print(is_prime(1331))
