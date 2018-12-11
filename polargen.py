import random
import math 
import matplotlib.pyplot as plot
import numpy as np
import scipy.stats as stats

class PolarGenerator:
    def __init__(self, saved, savedNumber):
        self.saved = saved
        self.savedNumber = savedNumber

    def next(self):
        if(self.saved):
            while True:
                r1 = random.random()
                r2 = random.random()
                v1 = 2*r1-1
                v2 = 2*r2-1
                i = v1*v1+v2*v2
                if(1>i):
                    break
            
            r = math.sqrt((-2 * math.log(i)) / i)
            self.savedNumber = r*v2
            self.saved = not self.saved
            return r*r1
            
        else:
            self.saved = not self.saved
            return self.savedNumber
            

polargen = PolarGenerator(True, 0)
numbers = []

for i in range(15):
    numbers.append(polargen.next())
    print(numbers[i])

numbers.sort()
hmean = np.mean(numbers)
hstd = np.std(numbers)
pdf = stats.norm.pdf(numbers, hmean, hstd)

plot.plot(numbers,pdf)
plot.show()