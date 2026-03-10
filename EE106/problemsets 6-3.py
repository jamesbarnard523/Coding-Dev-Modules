x = input('enter a sentence to print the first word in capitals\n')

firstWord, rest = x.split(" ",1)
result = firstWord.upper()+" "+rest

print (result)
