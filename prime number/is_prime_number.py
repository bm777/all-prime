#################################################################################
#################################################################################
#################################################################################

# This file is to know if a number is a prime number




#################################################################################
import math
import random

def is_prime(number):
    state = True
    if number < 1 and number == 4:
        return False
    elif number == 2 or number == 3:
        return True
    else:
        for i in range(2, int(number/2)):
            if number % i == 0:
                state = False
                break
        return state

def pi(n):
    result = []
    for iter in range(n):
        if(is_prime(iter) == True):
            if iter % 100 == 0:
                print(result)
            result.append(iter)

    return len(result)





if __name__ == '__main__':
    print(pi(int(math.pow(10,14))))
    # print(is_prime(9))
