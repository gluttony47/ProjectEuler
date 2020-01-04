""" Each new term in the Fibonacci sequence is generated by 
adding the previous two terms. By starting with 1 and 2, 
the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence 
whose values do not exceed four million, find 
the sum of the even-valued terms. """

# Author: Monirul Islam Tahir


# make a function to create fibonacci series. input is the nth term
def fibonacci(term):
    out = []
    if term == 1:
        out.append(1)
        return 1
    elif term == 2:
        out.append(1)
        return 1
    else:
        result = fibonacci(term - 1) + fibonacci(term - 2)
        out.append(result)
        return result

# make a function that generates a list of fibonacci
# series upto a limit


def list_Fibo(limit):
    result = 0
    i = 1
    out = []
    while limit > result:
        result = fibonacci(i)
        out.append(result)
        i = i + 1
    out = out[:-1]  # removing the last element of the list because
    # while keeps running 1 extra time since result > limit
    # only in the last iteration
    return out

# a function to check each element for odd or even and sums only
# the even elements


def evensum(fibolist):
    result = 0
    for element in fibolist:
        if (element % 2 == 0):
            result = result + element
    return result


problem_limit = 4000000
print(list_Fibo(problem_limit))
print(f'result is {evensum(list_Fibo(problem_limit))}')

# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578]
# result is 4613732
