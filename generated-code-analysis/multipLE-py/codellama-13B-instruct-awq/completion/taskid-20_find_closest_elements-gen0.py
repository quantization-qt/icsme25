from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """


    # first iteration
    min_diff = abs(numbers[0] - numbers[1])
    min_pair = (numbers[0], numbers[1])

    for i in range(1, len(numbers)-1):
        diff = abs(numbers[i] - numbers[i+1])
        if diff < min_diff:
            min_diff = diff
            min_pair = (numbers[i], numbers[i+1])

    return min_pair
