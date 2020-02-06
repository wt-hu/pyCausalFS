# _*_code:utf_8_*_
#!/usr/bin/env python
# date:2019/9/10 20:18
import numpy as np


def Meek(DAG, pdag, Data):
    n, p = np.shape(Data)
    old_pdag = np.zeros((p, p))

    while not (pdag == old_pdag).all():
        old_pdag = pdag.copy()
        # rule 1
        X = [i for i in range(p) for j in range(p) if pdag[i, j] == -1]
        Y = [i for i in range(p) for j in range(p) if pdag[i, j] == -1]
        for i in range(len(X)):
            x = X[i]
            y = Y[i]
            Z = [j for j in range(p) if pdag[y, j] == 1 and DAG[x, j] == 0]
            for z in Z:
                pdag[y, z] = -1
                pdag[z, y] = 0
                DAG[y, z] = -1
                DAG[z, y] = -1

        # rule 2
        X = [i for i in range(p) for j in range(p)if pdag[i, j] == 1]
        Y = [j for i in range(p)for j in range(p)if pdag[i, j] == 1]
        if len(X) == 0:
            break
        for i in range(len(X)):
            x = X[i]
            y = Y[i]
        if np.any(np.multiply(
                np.array(pdag[x, :] == -1), np.array(pdag[:, y] == -1))):
            pdag[x, y] = -1
            pdag[y, x] = 0
            DAG[x, y] = -1
            DAG[y, x] = -1

        # rule 3
        X = [i for i in range(p) for j in range(p)if pdag[i, j] == 1]
        Y = [j for i in range(p)for j in range(p)if pdag[i, j] == 1]
        if len(X) == 0:
            break
        Z = [j for j in range(p)if pdag[x, j] == 1 and pdag[j, y] == -1]
        for i in Z:
            for j in Z:
                if i != j:
                    pdag[x, y] = -1
                    pdag[y, x] = 0
                    DAG[x, y] = -1
                    DAG[y, x] = -1

    return pdag


# C:\pythonProject\pyCausalFS\LSL\data\Child_s500_v1.csv
