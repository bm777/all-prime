#################################################################################
#################################################################################
#################################################################################

# This file is to know if a number is a prime number
#   - test division by 3, 5, 7.
#
#
#
#
#

#################################################################################
import math
import random

def is_prime(number):
    state = True
    if number <= 1 or number == 4:
        return False
    elif number == 2 or number == 3:
        return True
    else:
        for i in range(2, int(number/2)):
            if number % i == 0:
                state = False
                break
        return state

def is_primeV2(n):
    if(n<=3):
        return n > 1

    if (n%2 == 0 or n%3==0):
        return False
    i = 5
    while i ** 2 <= n:
        if(n % i==0 or n % (i+2)): return False
        i += 6



def prob(n):
    return 100 * 1 / (math.log(n))

def by_3(n):
    return True if sum([int(e) for e in str(n)]) % 3 == 0 else False

def by_2_5(n):
    return True if int(str(n)[-1]) in [0, 2, 4, 5, 6, 8] else False

def by_7(n):

    return True if n % 7 else False

def pi(start=0, end=0):
    result = []
    for iter in range(start,end):
        if(is_prime(iter) == True):
            result.append(iter)

    return len(result)




if __name__ == '__main__':
    # test division by 3, 3, 7
    # print(by_3(71112))
    # print(by_2(71111))
    # print(by_7(10000200121227))
    # print(prob(10000200121227))
    print(is_prime(pow(2,32) - 2))

    # test of goldach conjecture
    # M = int( math.pow(10,7) )
    # print(pi(start=M, end=3159+M))
