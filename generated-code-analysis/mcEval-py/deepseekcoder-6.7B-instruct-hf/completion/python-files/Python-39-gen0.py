def calculate_arrangements(n, m, a) -> int:
    """
    Compute the number of ways to arrange m pots of flowers using up to n types,
    where the ith type can have at most a[i] pots, and the arrangement must be in
    increasing order of flower types.

    Args:
    - n (int): The number of flower types available.
    - m (int): The total number of flower pots to arrange.
    - a (list of int): A list where a[i] is the maximum number of pots for the ith type of flower.

    Returns:
    - int: The number of distinct arrangements modulo (10^6 + 7).

    Examples:
    - calculate_arrangements(2, 4, [3, 2]) returns 2.
    - calculate_arrangements(3, 3, [1, 2, 3]) returns 6.
    """
    mod = int(1e6 + 7)

    fact = [0] * (n + m + 1)
    factinv = [0] * (n + m + 1)

    fact[0] = 1
    for i in range(1, n + m + 1):
        fact[i] = (fact[i - 1] * i) % mod

    factinv[-1] = pow(fact[-1], mod - 2, mod)
    for i in range(n + m - 1, -1, -1):
        factinv[i] = (factinv[i + 1] * (i + 1)) % mod

    def comb(n, k):
        if k < 0 or n < k:
            return 0
        return (fact[n] * factinv[k] % mod) * factinv[n - k] % mod

    def nCr(n, k):
        if n < k:
            return 0
        return fact[n] * factinv[n - k] % mod

    dp = [0] * (m + 1)
    dp[0] = 1
    s = [0] * (n + 1)
    s[0] = 1

    for i in range(1, n + 1):
        dp2 = dp[:]
        for j in range(a[i - 1] + 1):
            for k in range(m - j + 1):
                dp2[k + j] = (dp2[k + j] + dp[k] * comb(s[i] - 1, j)) % mod
        dp = dp2
        s[i] = s[i - 1] + a[i - 1] + 1

    return dp[m]
def test_calculate_arrangements():
    # Helper function to compare expected and actual results
    def assert_equal(actual, expected, message):
        assert actual == expected, message

    # Test Case 1
    n, m, a = 2, 4, [3, 2]
    expected = 2
    assert_equal(calculate_arrangements(n, m, a), expected, f"Test Case 1 failed: expected {expected}, got {calculate_arrangements(n, m, a)}")

    # Test Case 2
    n, m, a = 3, 3, [1, 2, 3]
    expected = 6
    assert_equal(calculate_arrangements(n, m, a), expected, f"Test Case 2 failed: expected {expected}, got {calculate_arrangements(n, m, a)}")

    # Test Case 3
    n, m, a = 1, 5, [5]
    expected = 1
    assert_equal(calculate_arrangements(n, m, a), expected, f"Test Case 3 failed: expected {expected}, got {calculate_arrangements(n, m, a)}")

    print("All tests passed!")

if __name__ == "__main__":
    test_calculate_arrangements()