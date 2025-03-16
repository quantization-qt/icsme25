
def max_energy(beads):
    """
    Calculate the maximum energy that can be released by merging beads on a necklace.

    The function takes a list of integers representing the energy beads on a necklace, where
    each bead has a head and a tail value. The head value of each bead must match the tail
    value of the next bead in the sequence. The necklace is circular, and merging two adjacent
    beads releases energy equal to the product of the head value of the first bead, the matching
    value, and the tail value of the second bead.

    To find the maximum energy release, the function considers all possible orders of merging beads
    and uses dynamic programming to compute the maximum energy obtainable.

    Args:
        beads: A list of integers where each integer represents the head value of a bead and
               the tail value of the previous bead. The tail value of the last bead is assumed
               to match the head value of the first bead due to the circular nature of the necklace.

    Returns:
        An integer representing the maximum energy that can be obtained by optimally merging all beads.

    Examples:
        >>> max_energy([2, 3, 5, 10])
        710
        >>> max_energy([1, 2, 3, 4])
        48
    """
    n = len(beads)
    max_val = 0
    memo = [[0] * (n - 1) for _ in range(n - 1)]

    # Consider all possible orders of merging two adjacent beads
    for i in range(n - 1):
        # Merge the first bead with the second
        max_val = max(max_val, beads[0] * beads[1] * beads[2])
        memo[0][i] = max_val
        # Merge the last bead with the second to last
        max_val = max(max_val, beads[-2] * beads[-1] * beads[0])
        memo[-1][i] = max_val

    # Consider all possible orders of merging three adjacent beads
    for i in range(n - 2):
        # Merge the first two beads with the third
        max_val = max(max_val, beads[0] * beads[1] * beads[2])
        memo[1][i] = max_val
        # Merge the last two beads with the second to last
        max_val = max(max_val, beads[-3] * beads[-2] * beads[-1])
        memo[-2][i] = max_val

    # Consider all possible orders of merging four adjacent beads
    for i in range(n - 3):
        max_val = max(max_val, beads[0] * beads[1] * beads[2] * beads[3])
        memo[2][i] = max_val
        max_val = max(max_val, beads[-4] * beads[-3] * beads[-2] * beads[-1])
        memo[-3][i] = max_val

    return max_val
def test_max_energy():
    assert max_energy([2, 3, 5, 10]) == 710, "Testcase 1 failed"
    assert max_energy([1, 2, 3, 4]) == 80, "Testcase 2 failed"
    assert max_energy([4, 4, 4, 4]) == 192, "Testcase 3 failed"
    assert max_energy([30, 40, 50, 60]) == 372000, "Testcase 4 failed"
    print("All testcases passed")

# Call the test function
test_max_energy()