import random

def generate_revenue_data(I, N):
    revenue_data = []
    # Append a row of zeros at the beginning
    revenue_data.append([0] * (N + 1))
    for i in range(1, I+1):
        row = [0] * (N + 1)  # Initialize row with zeros
        previous_row_value = 0
        for j in range(min(i, N) + 1):
            # Generate random revenue values within a range ensuring increasing values within each row and column
            if j == 0:
                row[j] = 0  # Zero values for invalid combinations
            else:
                min_val = previous_row_value + 0.1 if j > 1 else 0.1  # Ensure row-wise incrementality
                max_val = previous_row_value + 2.0
                row[j] = round(random.uniform(min_val, max_val), 2)
                previous_row_value = row[j]

        # Ensure column-wise incrementality
        for j in range(1, N + 1):
            if i > 1:
                row[j] = max(row[j], revenue_data[i - 1][j])

        revenue_data.append(row)
    return revenue_data

# Example usage:
I = 8
N = 7
revenue_data = generate_revenue_data(I, N)
for row in revenue_data:
    print(row)
