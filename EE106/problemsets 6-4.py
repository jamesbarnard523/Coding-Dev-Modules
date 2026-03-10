x = input('enter a sentence please:\t')
y = ''

for sentence in range(len(x)-1,-1,-1):
    y += x[sentence]


print(y)


