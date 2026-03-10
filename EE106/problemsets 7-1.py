x = input('enter a sentence to alphabetise:\n')

xsplit= x.split(' ')
s = sorted(xsplit)

symbol = ','
result = symbol.join(s)


print(result)
