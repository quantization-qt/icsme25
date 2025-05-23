from typing import List, Optional

def prod_signs(arr: List[int]) -> Optional[int]:
    """
    You are given an array arr of integers and you need to return
    sum of magnitudes of integers multiplied by product of all signs
    of each number in the array, represented by 1, -1 or 0.
    Note: return None for empty arr.

    Example:
    >>> prod_signs([1, 2, 2, -4])
    9
    >>> prod_signs([0, 1])
    0
    >>> prod_signs([])
    None
    """

    if not arr:
        return None
    product_of_signs = 1
    sum_of_magnitudes = 0
    for num in arr:
        if num < 0:
            product_of_signs *= -1
        elif num > 0:
            sum_of_magnitudes += num
    return product_of_signs * sum_of_magnitudes
