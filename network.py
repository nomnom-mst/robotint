import numpy as np
import neuron
import glob
from IPL import Image

_input[i] = np.random.rand(100)
answer[out_num] = [hoge]
w[k] = np.random.rand(100);
wo[k] = np.random.rand(100);

m_num = 50
out_num = 6


##loading teacher image
images = []
for name in glob.glob('image/*.jpg'):
    images.append(Image.open(name))

for image in images:
    image.show()    


##initial setting
for i in range(100):
    ni[i] = neuron.InputNeuron(_input[i])

for j in range(m_num):
    nm[j] = neuron.Neuron()
    for k in range(100):
        nm[j].connect(ni[k],w[k])

for j in range(out_num):
    no[j] = neuron.Neuron()
    no[j].generateDelta
    for k in range(m_num):
        no[j].connect(nm[k],wo[k])

for j in range(m_num):
    nm[j].calculateDelta


##learnig
for i in range(out_num):
    no[i].update( no[i].output - answer[j] )
