import numpy as np
from CBD.MBs.IAMB import IAMB
from LSL.MBs.common.condition_independence_test import cond_indep_test
from LSL.MBs.common.Meek import Meek
from CBD.MBs.common.subsets import subsets
import math

def MB_by_MB(data, target, alaph, is_discrete = True):
    n,p = np.shape(data)
    Donelist = []    # whose MBs have been found
    Waitlist = [target]    # whose MBs will be foundM
    G = np.zeros((p,p))    # 1 denotes ->, 0 denote no edges
    pdag = G.copy()        # -1 denotes ->, 0 denote no edges
    DAG = G.copy()         # 1 denote -,0 denote no edges
    MB = [[] for i in range(p)]
    sepset = [[[]] * p for i in range(p)]
    k = 3
    while Waitlist != []:
        stop = False
        Waitlist_temp = Waitlist.copy()
        for x in Waitlist_temp:
            spouse = [[] for i in range(p)]
            Donelist.append(x)
            Waitlist.remove(x)
            MB[x],_ = IAMB(data, x, alaph, is_discrete)
            for i in MB[x]:
                Waitlist.append(i)
            findflag = False
            for i in range(len(MB)):
                if set(MB[x]) < set(MB[i]):
                    findflag = True
                    break
            if set(MB[x]) <= set(Donelist):
                findflag = True
            if findflag:
                continue
            # find spouse and pc
            # print("find spouse and pc")
            pc = MB[x].copy()
            # print("MB is " + str(MB))
            for i in range(len(MB[x])):
                cutsetsize = 0
                break_flag = 0
                c = MB[x][i]
                # print("c is " + str(c))
                CanPC = [i for i in MB[x] if i != c]
                # print("CanPC is " + str(CanPC))
                while len(CanPC) >= cutsetsize and cutsetsize <= k:
                    SS = subsets(CanPC, cutsetsize)
                    # print("SS is " + str(SS))
                    for s in SS:
                        # print("s is " + str(s))
                        pval, _ = cond_indep_test(data, x, c, s,is_discrete)
                        # print("pval is " + str(pval))
                        if pval <= alaph:
                            continue
                        else:
                            sepset[x][c] = s
                            # print("sepset[x][c] is " + str(sepset[x][c]))
                            pc.remove(c)
                            break_flag = True
                            break
                    if break_flag:
                        break
                    cutsetsize += 1
            # print("pc is " + str(pc))
            rest = [i for i in MB[x] if i not in pc]
            # print("rest is " + str(rest))
            for i in range(len(rest)):
                for j in range(len(pc)):
                    if pc[j] in sepset[x][rest[i]]:
                        continue
                    condition = [str(m) for m in sepset[x][rest[i]]]
                    # print("before condition is " + str(condition))
                    condition = list(set(condition).union(set(str(rest[i]))))
                    # print("condition is " + str(condition))
                    pval, _ = cond_indep_test(data, rest[i], x, condition,is_discrete)
                    # print("pval is "+ str(pval))
                    if pval <= alaph or math.isnan(pval):
                        spouse[j].append(rest[i])

            # print("v-structure")
            # print("spouse is " + str(spouse))
            # construct v-strcture
            for i in range(len(pc)):
                b = pc[i]
                DAG[x, b] = 1; DAG[b, x] = 1
                if pdag[x, b] == 0 and pdag[b, x] == 0:
                    pdag[x, b] = 1;pdag[b, x] = 1
                    G[x, b] = 1;G[b, x] = 1
                if len(spouse[i]) > 0:
                    for j in range(len(spouse[i])):
                        c = spouse[i][j]
                        DAG[c,b] = 1;   DAG[b,c] = 1;    DAG[x,c] = 0; DAG[c,x] = 0
                        pdag[x,b] = -1; pdag[c,b] = -1; pdag[b,x] = 0; pdag[b,c] = 0; pdag[x,c] = 0; pdag[c,x] = 0
                        G[x,b] = 1;     G[c,b] = 1;     G[b,x] = 0;    G[b,c] = 0;    G[c,x] = 0;    G[x,c] = 0
                        # pdag[b, x] = -1;pdag[b, c] = -1;pdag[x, b] = 0;pdag[c, b] = 0;pdag[c, x] = 0;pdag[x, c] = 0
                        # G[b, x] = 1;G[b, c] = 1;G[x, b] = 0;G[c, b] = 0;G[x, c] = 0;G[c, x] = 0
            # oriented by meek approach
            # print("meek")
            pDAG = Meek(DAG, pDAG, data)
            # if all edges connected to T are oriented
            stop = True
            connect = [i for i in range(p) if DAG[target, i] == 1]  # all nodes connected to target
            # print("connect is " + str(connect))
            for i in connect:
                if pdag[target, i] != -1 and pdag[i, target] != -1:
                    stop = False
                    break
            if stop:
                break
        if stop:
            break
        # print("Donelist is " + str(Donelist))
        # print("Waitlist is " + str(Waitlist))
        Waitlist = list(set(Waitlist))
        for i in Donelist:
            if i in Waitlist:
                Waitlist.remove(i)
        # print("Waitlist is " + str(Waitlist))
    np.transpose(G)
    np.transpose(pdag)
    parents = [i for i in range(p) if pdag[i, target] == -1]
    children = [i for i in range(p) if pdag[target, i] == -1]
    undirected = [i for i in range(p) if pdag[target, i] == 1]
    return parents, children, undirected


# # data = pd.read_csv("F:\cai_algorithm\data\Child_s500_v1.csv")
# data = pd.read_csv("F:\cai_algorithm\Alarm_data\Alarm1_s500_v1.csv")
# # path = "F:\cai_algorithm\Alarm_data\Alarm1_s500_v1.txt"
# # data = np.loadtxt(path, dtype=None, delimiter= ' ')
# target = 0
# Graph, p, c = MB_by_MB(data,target,0.01)
# print("\nin the last -------------------------------------")
# print(Graph)
# print("target " + str(target) + " parents are " + str(p))
# print("target " + str(target) + " children are " + str(c))