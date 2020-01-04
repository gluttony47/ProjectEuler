# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

# author: Monirul Islam Tahir

# solution strategy:
# 1. we want largest prime factor
# 2. we need a list of prime numbers that are smaller than sqrt(given_number)

# a function to find largest prime factor


def LargestPrimeFactor(number):
    # looks like we need to generate a list of prime numbers first

    # a function to generate/find prime numbers upto a limit
    # -done - PrimeGenerator(number)
    divisor_list = PrimeGenerator(number)
    i = len(divisor_list)

    for elem in list(range(i-1, 0, -1)):
        if (number % divisor_list[elem] == 0):
            return divisor_list[elem]
    return 'nothing found'

# a function to generate a list of prime numbers upto sqrt(given number)


def PrimeGenerator(number):
    number = int(number**0.5)
    result = []
    print(f'i only need to generate prime numbers upto {number}')
    # looks like we need to go through some numbers and check if
    # a number is prime or not
    # make a function? - done - IsPrime()
    for i in range(2, number):
        if IsPrime(i):
            result.append(i)
    print(f'total primes found {len(result)}')
    return result


def IsPrime(number):
    if number <= 3:
        return number > 1
    elif (number % 2 == 0) or (number % 3 == 0):
        return False

    i = 5

    while (i*i <= number):
        if (number % i == 0) or (number % (i+2) == 0):
            return False
        i = i + 6

    return True


number = 600851475143
#number = 10001

print(f'so the largest prime factor is {LargestPrimeFactor(number)}')

# i only need to generate prime numbers upto 775146
# total primes found 62113
# so the largest prime factor is 6857
