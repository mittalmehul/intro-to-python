# Problem: Write a program which will find factors of given number and
#  find whether the factor is even or odd.

#  Assumptions: given number is a positive integer


def get_factors(num):
    if not num:
        return -1
    factors = [(1, 'odd')]
    iterator = 2
    while iterator <= num:
        if num%iterator == 0:
            factors.append((iterator, is_even(iterator)))
        iterator+=1
    return factors

def is_even(num):
    result = ['even', 'odd']
    return result[num%2]

# Driver function

print(get_factors(10))