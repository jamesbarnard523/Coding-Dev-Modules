x = int(input('enter your test score please:\t'))

if 100<=x>=81:
    print('Grade A')
elif x>=61:
    print('Grade B')
elif x>=41:
    print('Grade C') 
elif x>= 21:
    print('Grade D')
else:
    print ("Grade E")