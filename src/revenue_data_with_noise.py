import random
from pprint import pprint
from typing import List, Tuple, Dict
from prettytable import PrettyTable
from prettytable.colortable import ColorTable, Themes

def generate_revenue_data(I, N):
    revenue_data = []
    
    revenue_data.append([0] * (N + 1))
    for i in range(1, I+1):
        row = [0] * (N + 1)  
        previous_row_value = 0
        for j in range(min(i, N) + 1):
            if j == 0:
                row[j] = 0  
            else:
                min_val = previous_row_value + 0.1 if j > 1 else 0.1  
                max_val = previous_row_value + 2.0
                row[j] = round(random.uniform(min_val, max_val), 2)
                previous_row_value = row[j]
        
        for j in range(1, N + 1):
            if i > 1:
                row[j] = max(row[j], revenue_data[i - 1][j])

        revenue_data.append(row)
    return revenue_data

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
    return js, ms


def main():

    I = int(input("Enter the value of I:"))
    N = int(input("Enter the value of N:"))
    M = 2

    data = {}
    for m in range(1, M + 1):
        data[m] = generate_revenue_data(I, N)

    js, ms = calculateRevenue(data1=data, M=M, I=I, N=N, cost=0.15)

    print(f"The associated optimum decision is (j*, m*) = ({js},{ms}).")


if __name__ == "__main__":
    main()
