# Design a code that will find whether the given number is a Palindrome number or not.

def is_palindrome(num):
    rev_num = num[::-1]
    return True if num==rev_num else False
    
num = input("Enter a number: ")
if(is_palindrome(num)):
    print('palindrome')
else:
    print('not palindrome')