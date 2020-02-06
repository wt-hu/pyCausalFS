import pandas as pd
from scipy import stats, sqrt
import math
import time


def chi_square_test(df, var1, var2, condition_vars=None, alaph=0.01):
    """
    Test for the independence condition (var1 _|_ var2 | condition_vars) in df.

    Parameters
    ----------
    df: pandas Dataframe
        The dataset on which to test the independence condition.

    var1: str
        First variable in the independence condition.

    var2: str
        Second variable in the independence condition

    condition_vars: list
        List of variable names in given variables.

    Returns
    -------
    chi_stat: float
        The chi-square statistic for the test.

    p_value: float
        The p-value of the test

    dof: int
        Degrees of Freedom
    """
    var1 = str(var1)
    var2 = str(var2)
    if not condition_vars:
        observed = pd.crosstab(df[str(var1)], df[str(var2)])
        chi_stat, p_value, dof, expected = stats.chi2_contingency(observed)

    else:
        condition_vars = [str(i) for i in condition_vars]
        observed_combinations = df.groupby(condition_vars).size().reset_index()

        chi_stat = 0
        dof = 0
        for combination in range(len(observed_combinations)):
            df_conditioned = df.copy()
            for condition_var in condition_vars:
                df_conditioned = df_conditioned.loc[df_conditioned.loc[:,
                                                                       condition_var] == observed_combinations.loc[combination,
                                                                                                                   condition_var]]
            observed = pd.crosstab(df_conditioned[var1], df_conditioned[var2])
            chi, _, freedom, _ = stats.chi2_contingency(observed)
            chi_stat += chi
            dof += freedom
        p_value = 1.0 - stats.chi2.cdf(x=chi_stat, df=dof)
    # if dof <= 0:
    #     dof = 1
    if math.isnan(p_value):
        chi_stat = 1.0
        dep = 2.0 + chi_stat  # / dof
    elif p_value > alaph:
        dep = -2.0 - chi_stat  # / dof
    else:
        dep = 2.0 + chi_stat  # / dof

    # n = df.shape[0]
    # rmsea = sqrt((chi_stat / dof - 1) / (n - 1))

    p_value = round(p_value, 2)
    # if p_value > alaph:
    #     p_valueX, p_valueY = str(p_value).split('.')
    #     p_value = float(p_valueX + '.' + p_valueY[0:2])

    return chi_stat, p_value, dof, 1 - p_value

# df = pd.read_csv("C:/Users/wkb/PycharmProjects/mb_algorithm/data/Child_s500_v1.csv")
# start = time.time()
# chi_stat, pval, dof, dep = chi_square_test(df, "0", "6", ["1"])
# end = time.time()
# print(chi_stat)
# print(pval)
# print(dof)
# print(dep)
# print(end - start)
