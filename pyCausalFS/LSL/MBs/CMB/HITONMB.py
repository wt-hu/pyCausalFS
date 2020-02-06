from LSL.MBs.common.condition_independence_test import cond_indep_test
from LSL.MBs.CMB.HITONPC import HITON_PC


def HITON_MB(data, target, alaph, is_discrete):
    PC,sepset,ntest=HITON_PC(data,target,alaph,is_discrete)
    MB=PC.copy()
    for X in PC:
        ntest+=1
        pcofPC,_,ntest1=HITON_PC(data, X, alaph, is_discrete)
        ntest+=ntest1
        for Y in pcofPC:
            ntest+=1
            if Y!=target and Y not in PC:
                condition_vars=[str(i) for i in sepset[Y]]
                condition_vars.append(str(X))
                condition_vars=list(set(condition_vars))
                pval, _ = cond_indep_test(data, Y, target, condition_vars, is_discrete)
                if pval<=alaph:
                    MB.append(Y)

    return MB,PC

# data = pd.read_csv("E:/python/pycharm/algorithm/data/Child_s500_v1.csv")
# MB ,ntest= HITON_MB(data, 1, 0.01)
# print(MB)
# print(ntest)