import numpy as np
import neuron
import glob
from PIL import Image

m_num = 200
out_num = 6

_input = np.random.rand(100)
answer = [[1,0,0,0,0,0],[0,1,0,0,0,0],[0,0,1,0,0,0],[0,0,0,1,0,0],[0,0,0,0,1,0]]
w = np.random.normal(0,0.1,size=(m_num,100)) 
wo = np.random.normal(0,0.1,size=(out_num,m_num))

print w

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
    #nMiddle.append(neuron.Neuron(1.0/4000))
    nMiddle.append(neuron.Neuron(1.0))
    for k in range(100):
        nMiddle[j].connect(nInput[k],w[j][k])
####    print nMiddle[j].output()
for j in range(out_num):
    nOutput.append(neuron.Neuron(1.0))
    for k in range(m_num):
        nOutput[j].connect(nMiddle[k],wo[j][k])
    print nOutput[j].output()






##learning --?
print 'learning'
repeatNum = 10
for k in range(repeatNum):
    for j,image in enumerate(images):

        
    ### new data loading--OK
        for i,data in enumerate(image):
            nInput[i].refreshdata(data/255.0)
        


    ###delta --too small
        test3 = []
        for i in range(out_num):
            nOutput[i].generateDelta(nOutput[i].output() - answer[j][i])
            test3.append(nOutput[i].output() - answer[j][i])
        ####print test3
        ####    print nOutput[i].delta
            
        for neu in nMiddle :
            neu.calculateDelta()
           #### print neu.delta

    ###learning---maybe OK
        result2 = []
        for neu in nOutput :
            neu.update()
            result2.append(neu.output())
       #### print result2
            
    ###BPLearning
        for neu in nMiddle:
            neu.update()



##test---OK
print 'test now'
result = []
for image in images:
    for i ,data in enumerate(image):
        nInput[i].refreshdata(data)

    for i in range(out_num):
        result.append(nOutput[i].output())
    print result

    result = []
