""" If we list all the natural numbers below 10 that are 
multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of 
these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000. """

"""author: Monirul Islam Tahir"""

def threefive(limit):
    out = []
    sum_num = 0
    for number in range(limit):
        if (number % 3 == 0) or (number % 5 == 0):
            out.append(number)
            sum_num = sum_num + number
            print(f'{sum_num} -> {out}')
    print(f'I\'m done finding multiples of 3 or 5 upto {limit}' )
    print(f'\nThe total sum is {sum_num}')

threefive(1000)
print(f'I have solved the problem :)')