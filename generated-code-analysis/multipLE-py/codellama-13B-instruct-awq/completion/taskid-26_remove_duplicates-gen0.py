from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """

    # use a set to keep track of elements seen so far
    seen: set[int] = set()
    unique_nums: list[int] = []
    for num in numbers:
        if num not in seen:
            unique_nums.append(num)
            seen.add(num)
    return unique_nums
