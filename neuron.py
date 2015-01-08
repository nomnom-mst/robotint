import numpy as np

class Neuron:
    ETA = 0.5
    ALPHA = 2

    def __init__(self):
        self.prev = []
        self.prevcount = 0
        self.next =[]
        self.nextcount = 0
        self.delta = 0

    def output(self):
        u = 0.0
        for i in range(int(self.prevcount)):
            u += self.prev[i][0].output() * self.prev[i][1]
        return 1.0 / ( 1.0 + np.exp(-ALPHA*u))

    def generateDelta(self):
        dsigma = ALPHA * self.output() * (1-self.output())
        self.delta = diff * dsigma

    def calculateDelta(self):
        for i in range(int(self.nextcount)):
            self.delta += self.next[i][1] * self.next[i][0].delta
            dsigma = ALPHA * self.output() * (1-self.output())
            self.delta *= dsigma
                       
    def connect(self,x,w):
        self.prev.append([x,w])
        self.prevcount += 1
        x.connectNext(self,w)

    def connectNext(self,x,w):
        self.next.append([x,w])
        self.nextcount += 1

    def update(self,diff):
        for i in range(int(self.prevcount)):
            self.prev[i][1] -= ETA * self.delta * self.prev[i][0].output()
        
class InputNeuron(Neuron):

    def __init__(self,y):
        self.prev = y        
    
    def output(self):
        return self.prev
