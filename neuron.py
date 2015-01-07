import numpy as np

class Neuron:
    ETA = 0.5
    ALPHA = 2

    def __init__(self):
        self.prev = []
        self.count = 0

        
    def output(self):
        u = 0.0
        for i in range(int(self.count)):
            u += self.prev[i][0].output() * self.prev[i][1]

        return 1.0 / ( 1.0 + np.exp(-ALPHA*u))
                       
    def connectPrev(self,x,w):
        self.prev.append([x,w])
        self.count += 1

    def update(self,diff,w):
        dsigma = ALPHA * self.output() * (1-self.output())
        delta = diff * dsigma
        for i in range(int(self.count)):
            self.prev[i][1] -= ETA * delta * self.prev[i][0].output()
        
class InputNeuron(Neuron):

    def __init__(self,y):
        self.prev = y        
    
    def output(self):
        return self.prev
