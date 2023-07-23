#  Write a program,
#  which will find all the numbers between 1000 and 3000 (both included)
#  such that each digit of a number is an even number.
#  The numbers obtained should be printed in a comma-separated sequence
#  on a single line.

def is_even(num):
    return True if (num%2==0) else False

def is_even(num):
    return True if (num%2==0) else False

def all_even_digits(num):
    if not num:
        return True
    if not is_even(num):
        return False
    return all_even_digits(num//10)
    

output = []
for num in range(1000, 3001):
    if all_even_digits(num):
        output.append(str(num))
print(",".join(output))