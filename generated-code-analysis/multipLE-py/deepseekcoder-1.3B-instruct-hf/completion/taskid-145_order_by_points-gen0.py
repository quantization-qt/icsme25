from typing import List

def order_by_points(nums: List[int]) -> List[int]:
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12])
    [-1, -11, 1, -12, 11]
    >>> order_by_points([])
    []
    """

    def sum_of_digits(num: int) -> int:
        return sum(int(digit) for digit in str(num))

    return [num for _, num in sorted(enumerate(nums), key=lambda x: (sum_of_digits(x[1]), x[0]))]
