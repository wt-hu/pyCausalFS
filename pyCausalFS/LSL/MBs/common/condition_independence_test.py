#!/usr/bin/env python
# encoding: utf-8
"""
 @Time    : 2019/11/13 21:34
 @File    : independence_condition_test.py
 """

from CBD.MBs.common.chi_square_test import chi_square_test
from CBD.MBs.common.fisher_z_test import cond_indep_fisher_z
from CBD.MBs.common.chi_square_test import chi_square


def cond_indep_test(data, target, var, cond_set=[], is_discrete=True, selected = False, alpha=0.01):
    if is_discrete:
        # if selected:
        #     _, pval, _, dep = chi_square_test(data, target, var, cond_set, alpha)
        # else:
        _, _, dep, pval = chi_square(target, var, cond_set, data, alpha)
    else:
        _, _, pval = cond_indep_fisher_z(data, target, var, cond_set, alpha)
        if pval >= alpha:
            dep = - (1 - pval)
        else:
            dep = 1 - pval

    return pval, dep
