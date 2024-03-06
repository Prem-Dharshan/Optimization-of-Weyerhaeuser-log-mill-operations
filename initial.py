from pprint import pprint

# dict of 2d lists
data1 = {
    1: [
        [1.00, 0, 0, 0, 0],
        [1.10, 1.15, 0, 0, 0],
        [1.40, 1.60, 2.80, 0, 0],
        [1.90, 1.90, 3.90, 4.10, 0],
        [2.10, 2.90, 4.40, 4.80, 7.20],
        [2.10, 3.50, 4.70, 6.10, 8.30],
    ],
    2: [
        [1.10, 0, 0, 0, 0],
        [1.10, 2.30, 0, 0, 0],
        [1.33, 2.40, 3.40, 0, 0],
        [2.10, 3.30, 4.20, 4.10, 0],
        [2.20, 3.60, 4.30, 4.60, 6.00],
        [2.20, 4.50, 4.40, 5.00, 6.30],
    ],
}

# length of a row in 2d list.
row_len = len(data1[1][0])


# print(M)
# cost matrix function which takes length of row in matrix, I = max val of i, cost given in ques as arguments
def costMatrix(row_len, I, cost):
    # initialising the 2d list with zeros
    c = [[0] * row_len for i in range(I)]

    for i in range(0, I):
        for j in range(0, row_len):
            if j < i:
                c[i][j] = cost

    # pprint(c)
    return c


# c = costMatrix(5,6,0.15)
# # costMatrix(M,6,0.15)
# print(c)


def calculateRevenue(M, I, N, cost):
    f = [0] * (I + 1)
    for m in range(1, M + 1):
        for i in range(1, I + 1):
            for j in range(1, min(i, N) + 1):
                if j < i:
                    c = cost
                else:
                    c = 0
                total = max(data1[m][i][j] - c + f[i - j])
                max_revenue = total
            f[i] = max_revenue

    print(f)


calculateRevenue(2, 6, 5, 0.15)
