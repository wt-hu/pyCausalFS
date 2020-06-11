# coding=utf-8
# /usr/bin/env python
"""
date: 2019/7/17 17:00
desc: 
"""
from CBD.MBs.common.condition_independence_test import cond_indep_test
from CBD.MBs.HITON.HITON_PC import HITON_PC


def HITON_MB(data, target, alaph, is_discrete=True):

    PC, sepset, ci_number = HITON_PC(data, target, alaph, is_discrete)
    # print("PC is:" + str(PC))
    currentMB = PC.copy()
    for x in PC:
        # print("x is: " + str(x))
        PCofPC, _,  ci_num2= HITON_PC(data, x, alaph, is_discrete)
        ci_number += ci_num2
        # print("PCofPC is " + str(PCofPC))
        for y in PCofPC:
            # print("y is " + str(y))
            if y != target and y not in PC:
                conditions_Set = [str(i) for i in sepset[y]]
                conditions_Set.append(str(x))
                conditions_Set = list(set(conditions_Set))
                ci_number += 1
                pval, dep = cond_indep_test(data, target, y, conditions_Set, is_discrete, True)
                if pval <= alaph:
                    # print("append is: " + str(y))
                    currentMB.append(y)
                    break

    return list(set(currentMB)), ci_number


# data = pd.read_csv("C:/pythonProject/pyCausalFS/data/child_s500_v1.csv")
# print("the file read")
#
# target = 4
# alaph = 0.05
#
# MBs=HITON_MB(data,target,alaph)
# print("MBs is: "+str(MBs))


# 500

# F1 is: 0.8465906593406597
# Precision is: 0.8957857142857146
# Recall is: 0.85525
# time is: 27.555


# 5000

# F1 is: 0.98
# Recall is: 0.99
# Distance is: 0.03
# ci_number is: 1017.85
# time is: 96.69