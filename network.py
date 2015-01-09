import numpy as np
import neuron
import glob
from PIL import Image

## parameter
repeatNum = 10
m_num = 10
out_num = 6
noiseProb = 0.1

## initial dummy data
_input = np.random.rand(100)
w = np.random.normal(0,0.1,size=(m_num,100)) 
wo = np.random.normal(0,0.1,size=(out_num,m_num))
answer = [[1,0,0,0,0,0],[0,1,0,0,0,0],[0,0,1,0,0,0],[0,0,0,1,0,0],[0,0,0,0,1,0],[0,0,0,0,0,1]]

##define noise generator function
def NoiseGenerator(data):
    noise = 255 * np.random.rand()
    prob = np.random.rand()
    if prob > 1-noiseProb:
        data = noise
    return data

##loading teacher image  --- OK
images = []
for name in glob.glob('image/*.jpg'):
    images.append(Image.open(name).convert('L').getdata())
    print name


##initial setting --- OK
print 'initialize'
nInput = []
nMiddle = []
nOutput = []
for i in range(100):
    nInput.append( neuron.InputNeuron(_input[i]) )
    
for j in range(m_num):
    nMiddle.append(neuron.Neuron(1.0))
    for k in range(100):
        nMiddle[j].connect(nInput[k],w[j][k])

for j in range(out_num):
    nOutput.append(neuron.Neuron(1.0))
    for k in range(m_num):
        nOutput[j].connect(nMiddle[k],wo[j][k])
    print nOutput[j].output() ####Printing initial output


##learning --OK
print 'learning now'
for k in range(repeatNum):
    for j,image in enumerate(images):

        
    ### new data loading--OK
        for i,data in enumerate(image):
            data = NoiseGenerator(data)
            nInput[i].refreshdata(data/255.0)
      
    ### delta --too small
        for i in range(out_num):
            nOutput[i].generateDelta(nOutput[i].output() - answer[j][i])
            
        for neu in nMiddle :
            neu.calculateDelta()

    ###learning---maybe OK
        for neu in nOutput :
            neu.update()
                    
    ###BPLearning
        for neu in nMiddle:
            neu.update()

print 'finish learning'


##test---OK
print 'test now'
for image in images:
    result = []

    for i ,data in enumerate(image):
        nInput[i].refreshdata(data)

    for i in range(out_num):
        result.append(nOutput[i].output())
    print result
