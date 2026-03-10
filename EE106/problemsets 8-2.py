


def expo(x):
    result = 0
   
    def fact(i):
        denominator = 1
        for y in range(1,i+1):
            denominator = denominator * y
        return denominator
        
    
        

    for i in range (50):
        numerator = x **i 
        result += numerator / fact(i)
    
    return result
 

    



x = float(input('enter a value to check for its exponential:\n'))

expo_result = expo(x)

print (f'expo of {x} = {expo_result}')