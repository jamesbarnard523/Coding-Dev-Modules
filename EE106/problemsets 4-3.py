x = float(input('enter an integer:\n'))

result = 0

for i in range (0,50,2):
    numerator = x **i 

    denominator = 1

    for y in range(1,i+1):
        denominator = denominator * y

    result+= numerator / denominator 

print (result)

