#!/usr/bin/env python
# encoding: utf-8
"""
 @Time    : 2019/10/17 16:36
 @File    : eva_classifier.py
 """

from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
import pandas as pd
import scipy
from scipy import io
from CBD.MBs.MMMB.MMMB import MMMB
from CBD.MBs.HITON.HITON_MB import HITON_MB
from CBD.MBs.PCMB.PCMB import PCMB
from CBD.MBs.IPCMB.IPCMB import IPC_MB
from CBD.MBs.GSMB import GSMB
from CBD.MBs.IAMB import IAMB
from CBD.MBs.fast_IAMB import fast_IAMB
from CBD.MBs.inter_IAMB import inter_IAMB
from CBD.MBs.IAMBnPC import IAMBnPC
from CBD.MBs.interIAMBnPC import interIAMBnPC
from CBD.MBs.STMB import STMB
from CBD.MBs.BAMB import BAMB
from CBD.MBs.FBEDk import FBED
from CBD.MBs.MBOR import MBOR
from CBD.MBs.LCMB import LRH
import numpy as np
import warnings



def eva_classifier(train_data,train_label,test_data, test_label, MB):

    # use MB and data  to train classifer clf
    X_train = train_data[:, MB]
    clf = SVC()
    clf.fit(X_train, train_label)
    Y_lable = clf.predict(test_data[:, MB])
    # precision, recall, fscore, _ = metrics.precision_recall_fscore_support(test_label, Y_lable, average='macro')
    accuracy = accuracy_score(test_label,Y_lable)
    return accuracy

if __name__ == '__main__':
    warnings.filterwarnings("ignore")

    data_labels = scipy.io.loadmat('D:/jerry/data/arcene/data_labels.mat')
    print(data_labels['data'].shape)
    # data_labels
    data_prime = data_labels['data']

    label = data_labels['labels']
    # label = data_labels['data'][:, 57]
    cv_indices = scipy.io.loadmat('D:/jerry/data/arcene/cv10_indices.mat')
    indices = cv_indices['indices']

    all_accuracy = [0] * 7
    method_list = ["IAMB", "inter_IAMB", "HITON_MB", "MMMB", "FBEDk", "GSMB"]
    #"IAMB", "inter_IAMB", "HITON_MB", "MMMB", "FBEDk", "GSMB"
    alaph = 0.01
    k = 5
    is_discrete = True
    for m in range(1, 11):
        test_indices = [i for i, j in enumerate(indices) if j == m]
        train_indices = [i for i, j in enumerate(indices) if j != m]
        train_data = data_prime[train_indices]
        train_label = label[train_indices]
        test_data = data_prime[test_indices]
        test_label = label[test_indices]
        data1 = pd.concat([pd.DataFrame(train_data), pd.DataFrame(train_label)], axis=1, ignore_index=True)
        #  Best of a bad bunch
        data1.to_csv('D:/temp/data_labels.csv', index=False)
        data = pd.read_csv('D:/temp/data_labels.csv')

        number, nver = np.shape(data)
        target = nver - 1
        print(number)
        train_indices = []
        test_indices = []

        for index, method in enumerate(method_list):
            print(target)
            print(method)
            if method == "MMMB":
                MB, ci_num = MMMB(data, target, alaph, is_discrete)
            elif method == "IAMB":
                MB, ci_num = IAMB(data, target, alaph, is_discrete)
            elif method == "IAMBnPC":
                MB, ci_num = IAMBnPC(data, target, alaph, is_discrete)
            elif method == "inter_IAMB":
                MB, ci_num = inter_IAMB(data, target, alaph, is_discrete)
            elif method == "interIAMBnPC":
                MB, ci_num = interIAMBnPC(data, target, alaph, is_discrete)
            elif method == "fast_IAMB":
                MB, ci_num = fast_IAMB(data, target, alaph, is_discrete)
            elif method == "GSMB":
                MB, ci_num = GSMB(data, target, alaph, is_discrete)
            elif method == "HITON_MB":
                MB, ci_num = HITON_MB(data, target, alaph, is_discrete)
            elif method == "PCMB":
                MB, ci_num = PCMB(data, target, alaph, is_discrete)
            elif method == "IPCMB":
                MB, ci_num = IPC_MB(data, target, alaph, is_discrete)
            elif method == "STMB":
                MB, ci_num = STMB(data, target, alaph, is_discrete)
            elif method == "IAMBnPC":
                MB, ci_num = IAMBnPC(data, target, alaph, is_discrete)
            elif method == "BAMB":
                MB, ci_num = BAMB(data, target, alaph, is_discrete)
            elif method == "FBEDk":
                MB, ci_num = FBED(data, target, k, alaph, is_discrete)
            elif method == "MBOR":
                MB, ci_num = MBOR(data, target, alaph, is_discrete)
            elif method == "LRH":
                MB, ci_num = LRH(data, target, alaph, is_discrete)
            else:
                raise Exception("method input error!")
            MB = sorted(MB)
            print("MB is: ", MB)
            if MB == []:
                print("error")
                continue
            accuracy = eva_classifier(train_data, train_label, test_data, test_label, MB)
            print("accuracy is: ", accuracy)
            all_accuracy[index] += accuracy

    with open('./output/true_indi_1.txt', "a+") as file:
        for i, method in enumerate(method_list):
            file.write(str(method)+":\n")
            file.write("f1 is:" + str("%.3f" % (all_accuracy[i]/10))+"\n")
            print(str(method), " end")
