# coding=utf-8
# /usr/bin/env python
"""
date: 2019/7/15 9:57
desc: 
"""
from CBD.MBs.MMMB.MMPC import MMPC
from CBD.MBs.common.condition_independence_test import cond_indep_test


def MMMB(data, target, alaph, is_discrete=True):
    ci_number = 0
    PC,sepset, ci_num2 = MMPC(data, target, alaph, is_discrete)
    ci_number += ci_num2
    # print("PC is: " + str(PC))
    # print("sepset is: " + str(sepset))
    MB = PC.copy()
    for x in PC:
        # print(x)
        PCofPC,_,ci_num3 = MMPC(data, x, alaph, is_discrete)
        ci_number += ci_num3
        # print("PCofPC is: " + str(PCofPC))
        for y in PCofPC:
            # print("_-++++++-_")
            if y != target and y not in PC:
                conditions_Set = [str(i) for i in sepset[y]]
                conditions_Set.append(str(x))
                conditions_Set = list(set(conditions_Set))
                ci_number += 1
                pval, dep = cond_indep_test(data, target, y, conditions_Set, is_discrete)
                # print("_----_")
                if pval <= alaph:
                    MB.append(y)
                    break
    return list(set(MB)), ci_number

# import pandas as pd
# data = pd.read_csv("C:/pythonProject/pyCausalFS/data/child_s500_v3.csv")
# print("the file read")
#
# target = 10
# alaph = 0.05
#
# MBs=MMMB(data,target,alaph)
# print("MBs is: "+str(MBs))


# F1 is: 0.7791296481296481
# Precision is: 0.8212976190476191
# Recall is: 0.796958333333333
# time is: 36.05296875

# 5000

# F1 is: 0.93 ±0.30
# Precision is: 0.90±0.26
# Recall is: 0.99±0.45
# Distance is: 0.11±0.39
# ci_number is: 1097.80±2499.40
# time is: 93.20±347.69
#

