# Wrixte a program that accepts a sentence and calculates the number of letters and digits.
# Suppose the entered string is:
#     Python0325 
# Then the output will be:
#     LETTERS: 6
#     DIGITS:4

def count_alphabets(string):
    letters= 0
    digits = 0
    for char in string:
        if char.isalpha():
            letters+=1
        elif char.isnumeric():
            digits+=1
    print('LETTERS: ', letters)
    print('DIGITS: ', digits)
    
string = input('Write Something: ')
count_alphabets(string)