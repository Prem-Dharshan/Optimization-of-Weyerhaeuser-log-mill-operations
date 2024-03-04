def max_revenue(L, K, M, R, c):
    # Initialize an array to store maximum revenue for each stem length
    f = [0] * (L // K + 1)

    # Iterate over all possible stem lengths
    for i in range(1, len(f)):
        # Initialize the maximum revenue for current stem length
        max_rev = 0

        # Determine the maximum number of logs that can be cut from the current stem length
        max_logs = min(i, len(R[1]))

        # Iterate over all possible log lengths
        for j in range(1, max_logs + 1):
            try:
                # Calculate revenue for current log length
                revenue = max(
                    [R[m][i][j] - c[i][j] + f[i - j] for m in range(1, M + 1)]
                )
            except KeyError:
                # Handle KeyError if the crosscut cost matrix doesn't have the required indices
                revenue = float("-inf")

            # Update maximum revenue if the current revenue is higher
            max_rev = max(max_rev, revenue)

        # Store the maximum revenue for the current stem length
        f[i] = max_rev

    return f


# Example usage
L = 12  # Length of the tree in feet
K = 2  # Minimum log length in feet
M = 2  # Number of mills
R = {
    1: {1: {1: 0, 2: 2, 3: 3, 4: 4}},  # Revenue matrix for mill 1
    2: {1: {1: 0, 2: 3, 3: 4, 4: 5}},  # Revenue matrix for mill 2
}
c = {1: {1: 0, 2: 0, 3: 0, 4: 0}, 2: {1: 0, 2: 0, 3: 0, 4: 0}}  # Crosscut cost matrix

# Calculate maximum revenue for each stem length
max_revenue = max_revenue(L, K, M, R, c)
print(max_revenue)
