import numpy as np

class Neuron:
    ETA = 0.5
   

    def __init__(self,ALPHA):
        self.prev = []
        self.prevcount = 0
        self.next =[]
        self.nextcount = 0
        self.delta = 0
        self.ALPHA = ALPHA
      

    def output(self):
        u = 0.0
        for i in range(int(self.prevcount)):
            u += self.prev[i][0].output() * self.prev[i][1]
####        print u*self.ALPHA
        return 1.0 / ( 1.0 + np.exp(-self.ALPHA*u))

    def generateDelta(self,diff):
        dsigma = self.ALPHA * self.output() * (1-self.output())
        self.delta = diff * dsigma ##diff
      
    def calculateDelta(self):
        for i in range(int(self.nextcount)):
            self.delta += self.next[i][1] * self.next[i][0].delta
            dsigma = self.ALPHA * self.output() * (1-self.output())
        self.delta *= dsigma
                       
    def connect(self,x,w):
        self.prev.append([x,w])
        self.prevcount += 1
        x.connectNext(self,w)

    def connectNext(self,x,w):
        self.next.append([x,w])
        self.nextcount += 1

    def update(self):
        for i in range(int(self.prevcount)):
    ####        print self.prev[i][1] ,self.ETA * self.delta * self.prev[i][0].output()
            self.prev[i][1] -= self.ETA * self.delta * self.prev[i][0].output()
        
class InputNeuron(Neuron):

    def __init__(self,y):
        self.prev = y        
    
    def output(self):
        return self.prev

    def connectNext(self,x,w):
        pass

    def refreshdata(self,data):
        self.prev = data
