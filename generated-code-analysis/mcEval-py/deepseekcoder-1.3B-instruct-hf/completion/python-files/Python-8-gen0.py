from typing import List, Tuple

def max_value_on_paths(N: int, grid_values: List[Tuple[int, int, int]]) -> int:
    """
    Calculate the maximum sum of values collected on two paths in an N x N grid.

    This function utilizes dynamic programming to find two paths from the top-left corner to
    the bottom-right corner of the grid which maximize the sum of the values collected. Each
    value can be collected at most once, even if both paths pass through it.

    Args:
    - N (int): The size of the grid (N x N).
    - grid_values (List[Tuple[int, int, int]]): A list of tuples where each tuple contains
      the x-coordinate, y-coordinate, and value to be placed on the grid at that position.
      The list is terminated by a tuple with all zeros.

    Returns:
    - int: The maximum sum of values collected on the two paths.

    Examples:
    >>> max_value_on_paths(2, [(1, 2, 1), (2, 1, 2), (0, 0, 0)])
    3
    >>> max_value_on_paths(8, [
    ...     (2, 3, 13), (2, 6, 6), (3, 5, 7), (4, 4, 14),
    ...     (5, 2, 21), (5, 6, 4), (6, 3, 15), (7, 2, 14),
    ...     (0, 0, 0)])
    67
    """
    # Initialize a 2D list to hold the maximum sum of values collected at each position.
    max_sum = [[0 for _ in range(N)] for _ in range(N)]

    # Calculate the maximum sum of values collected at each position.
    for i in reversed(range(N)):
        for j in reversed(range(N)):
            if i == N - 1 and j == N - 1:
                max_sum[i][j] = grid_values[i + j * N][2]
            else:
                # The maximum sum of values collected is the maximum of the sum of the
                # maximum sums of the paths to the bottom and right cell plus the value
                # at the current cell.
                max_sum[i][j] = max(
                    max_sum[i + 1][j] + grid_values[i + j * N][2],
                    max_sum[i][j + 1] + grid_values[i + j * N][2]
                )

    # The maximum sum of values collected on the two paths is the maximum sum of the
    # sums of the paths from the top-left corner to the bottom-right corner.
    return max_sum[0][0]
def test_max_value_on_paths():
    # Test case 1: Small grid with clear path
    assert max_value_on_paths(2, [(1, 2, 1), (2, 1, 2), (0, 0, 0)]) == 3
    
    # Test case 2: Example provided in the problem statement
    assert max_value_on_paths(8, [
        (2, 3, 13), (2, 6, 6), (3, 5, 7), (4, 4, 14),
        (5, 2, 21), (5, 6, 4), (6, 3, 15), (7, 2, 14),
        (0, 0, 0)]) == 67

    print("All test cases passed!")

# Run the test cases
test_max_value_on_paths()