x = int(input('enter an integer between -100 and 100\t'))

if x > 0:
    s = 'positive'
elif x < 0:
    s = 'negative'
else:
    s = 0

y = 'even' if (x%2==0) else 'odd'

print(f'integer value entered is {s} and,{y}')




