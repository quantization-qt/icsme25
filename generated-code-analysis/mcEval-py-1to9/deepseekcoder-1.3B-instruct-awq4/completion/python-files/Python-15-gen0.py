def optimize_seating(M: int, N: int, K: int, L: int, D: int, chatting_pairs: list) -> (str, str):
    """
    Optimize the placement of aisles in a classroom to minimize the amount of chatting between students.

    Args:
    M (int): The number of rows in the classroom.
    N (int): The number of columns in the classroom.
    K (int): The number of horizontal aisles to add.
    L (int): The number of vertical aisles to add.
    D (int): The number of chatting pairs in the classroom.
    chatting_pairs (list of tuples): A list of tuples, each containing the positions (Xi, Yi) and (Pi, Qi) of a chatting pair.

    Returns:
    (str, str): Two space-separated strings representing the optimal row and column indices for the aisles.

    The function works by counting the number of chatting pairs that can be separated by adding an aisle in each possible position.
    It then selects the most effective positions for aisles, aiming to separate as many chatting pairs as possible.

    Examples:
    - optimize_seating(4, 5, 1, 2, 3, [(4, 2, 4, 3), (2, 3, 3, 3), (2, 5, 2, 4)])
    Returns: ('2', '2 4')

    - optimize_seating(3, 3, 1, 1, 2, [(1, 2, 1, 3), (2, 1, 3, 1)])
    Returns: ('2', '2')
    """

    # Check for the base case
    if M == 1 and N == 1:
        return "0 0", "0 0"

    chatting_pairs.sort(key=lambda x: x[2] - x[0])  # Sort the chatting pairs based on Xi-Pi
    aisle_rows = ['0'] * (M + L)
    aisle_cols = ['0'] * (N + K)

    # Add the aisles
    for pair in chatting_pairs:
        xi, yi, pi, qi = pair
        aisle_rows[qi - 1] = '1'
        aisle_cols[xi - 1] = '1'

    # Calculate the number of aisles that can be placed in each row and column
    aisle_rows_count = [sum(aisle_rows[i:j]) for i in range(len(aisle_rows)) for j in range(i + 1, len(aisle
        ) + 1) if j - i > qi - xi]
        aisle_cols_count = [sum(aisle_cols[i:j]) for i in range(len(aisle_cols)) for j in range(i + 1, len(aisle_cols) + 1) if j - i > pi - yi]

    # Find the position of the aisles with the maximum count
    max_count = max(max(aisle_rows_count), max(aisle_cols_count))
    if max_count == 0:
        return "0 0", "0 0"

    optimal_row = aisle_rows_count.index(max_count) + qi
    optimal_col = aisle_cols_count.index(max_count) + xi

    return str(optimal_row), str(optimal_col)
def test_optimize_seating():
    test_cases = [
        # Test case 1 from the provided example
        {
            'M': 4, 'N': 5, 'K': 1, 'L': 2, 'D': 3,
            'chatting_pairs': [(4, 2, 4, 3), (2, 3, 3, 3), (2, 5, 2, 4)],
            'expected': ('2', '2 4')
        },
        # Corrected Test case 2
        {
            'M': 5, 'N': 6, 'K': 2, 'L': 3, 'D': 4,
            'chatting_pairs': [(1, 1, 1, 2), (2, 2, 3, 2), (4, 5, 4, 6), (5, 1, 5, 2)],
            'expected': ('1 2', '1 2 5')  # Corrected expected output
        },
        # Test case 3
        {
            'M': 3, 'N': 3, 'K': 1, 'L': 1, 'D': 2,
            'chatting_pairs': [(1, 2, 1, 3), (2, 1, 3, 1)],
            'expected': ('2', '2')
        },
    ]

    for i, test in enumerate(test_cases, 1):
        row_output, col_output = optimize_seating(
            test['M'], test['N'], test['K'], test['L'], test['D'], test['chatting_pairs']
        )
        assert row_output == test['expected'][0], f"Test case {i} failed: row_output {row_output} does not match expected {test['expected'][0]}"
        assert col_output == test['expected'][1], f"Test case {i} failed: col_output {col_output} does not match expected {test['expected'][1]}"
        print(f"Test case {i} passed.")

# Run the test function
test_optimize_seating()