import pandas as pd
import numpy as np

for i in range(11):
    j = 1
    if j == 1:
        snum = 500
    elif j == 2:
        snum = 1000
    elif j == 3:
        snum = 5000
    if i == 0:
        continue
    txt = np.loadtxt('D:/data/ins5_data/Insurance5_s'+str(snum)+"_v"+str(i)+'.txt')
    txtDF = pd.DataFrame(txt)
    txtDF.to_csv('D:/data/ins5_data/Insurance5_s'+str(snum)+"_v"+str(i)+'.csv', index=False)