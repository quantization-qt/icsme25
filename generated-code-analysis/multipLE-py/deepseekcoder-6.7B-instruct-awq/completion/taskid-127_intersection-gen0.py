from typing import Tuple

def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    """You are given two intervals,
    where each interval is a pair of integers. For example, interval = (start, end) = (1, 2).
    The given intervals are closed which means that the interval (start, end)
    includes both start and end.
    For each given interval, it is assumed that its start is less or equal its end.
    Your task is to determine whether the length of intersection of these two 
    intervals is a prime number.
    Example, the intersection of the intervals (1, 3), (2, 4) is (2, 3)
    which its length is 1, which not a prime number.
    If the length of the intersection is a prime number, return "YES",
    otherwise, return "NO".
    If the two intervals don't intersect, return "NO".


    [input/output] samples:
    >>> intersection((1, 2), (2, 3))
    'NO'
    >>> intersection((-1, 1), (0, 4))
    'NO'
    >>> intersection((-3, -1), (-5, 5))
    'YES'
    """

    # sort the intervals by their start
    intervals = sorted([interval1, interval2])
    # if the start of the second interval is later than the end of the first interval, they don't intersect
    if intervals[1][0] > intervals[0][1]:
        return 'NO'
    # if they intersect, the intersection is the interval starting at the later start and ending at the earlier end
    intersection = (max(intervals[0][1], intervals[1][1]), min(intervals[0][1], intervals[1][1]))
    # the length of the intersection is its end minus its start
    length = intersection[1] - intersection[0]
    # check if the length is a prime number
    if length < 2:
        return 'NO'
    for i in range(2, int(length ** 0.5) + 1):
        if length % i == 0:
            return 'NO'
    return 'YES'
