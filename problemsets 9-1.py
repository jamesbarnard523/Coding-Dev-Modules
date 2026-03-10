class Parallel:
    def __init__(self,r1,r2,r3):
        self.res1 = r1
        self.res2 = r2
        self.res3 = r3

        

    def getResist(self):
        total = 1/self.res1 + 1/self.res2 + 1/self.res3
        total = 1/total 
        return total
    
resistors = Parallel( 10,20,30)

print (f'resistance of resistors connected in parallel is :\n {resistors.getResist():.3f} ohms')

