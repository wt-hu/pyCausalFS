from pyBN.mmhc import mmhc
import pandas
import numpy as np


def example_mmhc(df):
    _, n = np.shape(df)
    data = np.array(df, dtype=np.int_)
    bn = mmhc(data)
    file = open("./output/output_mmhc.txt", "w+")
    print("\noutputs:\nthe key is the node,and the value is children.")
    file.write("outputs:\nthe key is the node,and the value is children.\n")
    file.write(str(bn))
    print(bn)


if __name__ == '__main__':

    data_path = input("data: ")
    if data_path == "default":
        data_path = "../SSD/data/Child_s500_v1.csv"
    data = pandas.read_csv(data_path)

    example_mmhc(data)
