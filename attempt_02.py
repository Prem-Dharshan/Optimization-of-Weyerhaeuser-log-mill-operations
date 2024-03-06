
from pprint import pprint
from typing import List, Tuple, Dict


def calculateRevenue (data1, M: int, I: int, N: int, cost: float):
    
    f: List[float] = [0] * (I + 1)
    f_array = [0] * (I + 1)
    total: int
    max_revenue: float = 0.0
    c: float
    js,ms = 0,0
    for i in range(1, I+1):
        for j in range(1, N+1):
            for m in range (1, M+1):
               
                if j < i:
                    c = cost
                else:
                    c = 0
                # print('tot', data1[m][i][j] - c + f[i - j], f'i={i}', f'j={j}' )
                total = data1[m][i][j] - c + f[i - j]
                if total > max_revenue:
                    max_revenue = total
                    js = j
                    ms = m
            f[i] = max_revenue
            f_array[i] = (js,ms)
   
    print(f)
    print(f_array)


def main():

    data = {
        1: [
            [0, 0   , 0   , 0   , 0   , 0   ],
            [0, 1.00, 0   , 0   , 0   , 0   ],
            [0, 1.10, 1.15, 0   , 0   , 0   ],
            [0, 1.40, 1.60, 2.80, 0   , 0   ],
            [0, 1.90, 1.90, 3.90, 4.10, 0   ],
            [0, 2.10, 2.90, 4.40, 4.80, 7.20],
            [0, 2.10, 3.50, 4.70, 6.10, 8.30],
        ],
        2: [
            [0, 0   , 0   , 0   , 0   , 0   ],
            [0, 1.10, 0   , 0   , 0   , 0   ],
            [0, 1.10, 2.30, 0   , 0   , 0   ],
            [0, 1.33, 2.40, 3.40, 0   , 0   ],
            [0, 2.10, 3.30, 4.20, 4.10, 0   ],
            [0, 2.20, 3.60, 4.30, 4.60, 6.00],
            [0, 2.20, 4.50, 4.40, 5.00, 6.30],
        ]
    }

    calculateRevenue(data1=data, M=2, I=6, N=5, cost=0.15)

if '__main__' == __name__:
    main()
