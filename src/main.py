from pprint import pprint
from typing import List, Tuple, Dict
from prettytable import PrettyTable
from prettytable.colortable import ColorTable, Themes
import pandas as pd


def calculateRevenue(data1, M: int, I: int, N: int, cost: float):

    calculations: List[PrettyTable] = []
    for table in range(M):
        calculations.append(ColorTable(theme=Themes.OCEAN))

    for i in range(M):
        calculations[i].field_names = ["j"] + [j for j in range(1, N + 1)]

    f: List[float] = [0] * (I + 1)
    f_array = [0] * (I + 1)
    total: int
    max_revenue: float = 0.0
    c: float
    js, ms = 0, 0

    arr = []
    for m in range(M):
        r_r = []
        for i in range(I):
            j_r = []
            for j in range(N):
                j_r.append(0)
            r_r.append(j_r)
        arr.append(r_r)

    for i in range(1, I + 1):

        for j in range(1, N + 1):

            for m in range(1, M + 1):

                if j < i:
                    c = cost
                else:
                    c = 0
                total = data1[m][i][j] - c + f[i - j]
                if total > max_revenue:
                    max_revenue = total
                    js = j
                    ms = m

                arr[m - 1][i - 1][j - 1] = round(total, 2)

            f[i] = round(max_revenue, 2)
            f_array[i] = (js, ms)

    for table in range(M):
        for row in range(I):
            calculations[table].add_row(
                [row + 1] + arr[table][row])

    print("\n")
    for i in range(M):
        print(f"CALCULATIONS FOR MILL {i+1}\n")
        print(calculations[i])
        print("\n\n")

    res: PrettyTable = ColorTable(theme=Themes.OCEAN)
    res.add_column("f(i)", f[1:])
    res.add_column("(j*, m*)", f_array[1:])

    print("\n\nREVENUE & CROSS CUTTING\n")
    print(res, "\n")


def read_excel_data(filename):
    data = {}
    xls = pd.ExcelFile(filename)
    for sheet_name in xls.sheet_names:
        data[int(sheet_name)] = pd.read_excel(
            filename, sheet_name=sheet_name, header=None).values.tolist()
    return data

def main():

    data = {
        1: [
            [0, 0, 0, 0, 0, 0],
            [0, 1.00, 0, 0, 0, 0],
            [0, 1.10, 1.15, 0, 0, 0],
            [0, 1.40, 1.60, 2.80, 0, 0],
            [0, 1.90, 1.90, 3.90, 4.10, 0],
            [0, 2.10, 2.90, 4.40, 4.80, 7.20],
            [0, 2.10, 3.50, 4.70, 6.10, 8.30],
        ],
        2: [
            [0, 0, 0, 0, 0, 0],
            [0, 1.10, 0, 0, 0, 0],
            [0, 1.10, 2.30, 0, 0, 0],
            [0, 1.33, 2.40, 3.40, 0, 0],
            [0, 2.10, 3.30, 4.20, 4.10, 0],
            [0, 2.20, 3.60, 4.30, 4.60, 6.00],
            [0, 2.20, 4.50, 4.40, 5.00, 6.30],
        ],
    }

    filename = input("Enter the Excel file name: ")
    data = read_excel_data(filename)

    pprint(data)

    M = int(input("Enter the value of M: "))
    I = int(input("Enter the value of I: "))
    N = int(input("Enter the value of N: "))
    COST = float(input("Enter the cost: "))

    calculateRevenue(data1=data, M=M, I=I, N=N, cost=COST)


if "__main__" == __name__:
    main()
