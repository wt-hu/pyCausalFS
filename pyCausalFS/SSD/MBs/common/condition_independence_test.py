#!/usr/bin/env python
# encoding: utf-8
"""
 @Time    : 2019/11/13 21:34
 @File    : independence_condition_test.py
 """

from CBD.MBs.common.chi_square_test import chi_square_test
from CBD.MBs.common.fisher_z_test import cond_indep_fisher_z


def cond_indep_test(data, target, var, cond_set=[], alpha=0.05, is_discrete=True):
    if is_discrete:
        _, pval, _, dep = chi_square_test(data, target, var, cond_set, alpha)
    else:
        _, _, pval = cond_indep_fisher_z(data, target, var, cond_set, alpha)
        dep = 1 - pval

    return pval, dep
