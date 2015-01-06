import numpy as np
import neauron


_input[i] =np.random.rand(100)
w[k] = np.random.rand(100)
m_num = 50
out_num = 6
    
for i in range(100):
    ni[i] = neauron.InputNeauron(_input[i])

for j in range(m_num):
    nm[j] = neauron.Neauron()
    for k in range(100):
        nm[j].connectInput(ni[k],w[k])

for j in range(out_num):
    no[j] = neauron.Neauron()
    for k in range(m_num):
        no[j].connectInput(nm[k],wo[k])

        
