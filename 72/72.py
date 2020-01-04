""" Consider the fraction, n/d, where n and d are positive integers.
If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending
 order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7,
3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set.

How many elements would be contained in the set of
reduced proper fractions for d ≤ 1,000,000? """

# author: Monirul Islam Tahir


def NumReducedProperFraction(number):
    result = []
    a = list(range(1, number+1))
    for i in a:
        l = a[::-1][:len(a)-i]
        for j in l:
            # write a function here to check HCF(n,d)==1 or not
            # -done-HCF(i,j)
            if (HCF(i, j)):
                result.append(f'{i}/{j}')
    return result




def HCF(i, j):
    if j < i:
        return False
    if i == 1 and j != 1:
        return True
    if j == 1:
        return False
    if (i % j == 0 or j % i == 0):
        return False
    if(i % 2 == 0 and j % 2 == 0):
        return False
    return True
# def gcd(a,b):
#     while b!= 0:
#         a,b = b, a%b
#     return a
# def coprime(a,b):
#     return gcd(a,b) ==1


num = 10000
result = NumReducedProperFraction(num)
# print(result)
print(f'total elements in list {len(result)}')
