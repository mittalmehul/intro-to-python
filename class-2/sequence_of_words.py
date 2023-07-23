# Problem: Write a code which accepts a sequence of words as input and prints the words in a sequence after sorting them alphabetically

sequence = input("Please enter a sequence of words, seperated by space: ")
sequence = sequence.split(' ')
sequence.sort()
result = ' '.join(sequence)
print("The words entered are as follows:")
print(result)