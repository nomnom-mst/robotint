import numpy as np

class Neauron:

    def __init__(self):
        self.input = []
        self.count = 0

        
    def output(self):
        u = 0.0
        for i in range(int(self.count)):
            u += self.input[i][0].output() * self.input[i][1]

        return 1.0 / ( 1.0 + np.exp(-u))
                       
    def connectInput(self,x,w):
        self.input.append([x,w])
        self.count += 1

class InputNeauron(Neauron):

    def __init__(self,y):
        self.input = y        
    
    def output(self):
        return self.input

    
    
##test

