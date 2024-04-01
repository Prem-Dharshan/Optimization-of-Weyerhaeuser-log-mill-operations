import random

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


I = int(input("Enter the value of I:"))
N = int(input("Enter the value of N:"))
revenue_data = generate_revenue_data(I, N)
for row in revenue_data:
    print(row)
