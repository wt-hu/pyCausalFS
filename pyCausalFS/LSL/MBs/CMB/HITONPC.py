from LSL.MBs.common.condition_independence_test import cond_indep_test
from LSL.MBs.common.subsets import subsets
import numpy as np


def HITON_PC(data, target, alaph, is_discrete):
    n,p=np.shape(data)
    PC=[]
    sepset=[[]for i in range(p)]
    CanPC=[i for i in range(p)if i!=target]
    ntest=0
    #print("canpc:",CanPC)
    while len(CanPC)>0:
        CanPC_temp=CanPC.copy()
        #print("canpc_temp:",CanPC_temp)
        #add the best candidata to PC
        for X in CanPC_temp:
            ntest+=1
            dep_max=-float("inf")
            attribute=0
            pval_temp=1.0
            pval, dep=cond_indep_test(data,X,target,[],is_discrete)
            if pval>alaph:
               CanPC.remove(X)
               continue
            elif dep>dep_max:
                dep_max=dep
                attribute=X
                pval_temp=pval
        if pval_temp<=alaph:
            PC.append(attribute)
            CanPC.remove(attribute)
        #remove true positives from PC
        PC_temp=PC.copy()
        for Y in PC_temp:
            ntest+=1
            k=0
            max_k=3
            breakflag=False
            nbrs=[i for i in PC if i !=Y]
            while k<=len(nbrs)and k<=max_k:
                SS=subsets(nbrs,k)
                for S in SS:
                    ntest+=1
                    pval, _ = cond_indep_test(data,target,Y,S, is_discrete)
                    if pval>alaph:
                        sepset[Y]=[i for i in S]
                        PC.remove(Y)
                        breakflag=True
                        break
                if breakflag:
                    break
                k+=1

    return PC,sepset,ntest

#data = pd.read_csv("E:/python/pycharm/algorithm/data/Child_s500_v1.csv")
#PC,sepset,ntest = HITON_PC(data, 1, 0.01)
#print(PC)
#print(ntest)



