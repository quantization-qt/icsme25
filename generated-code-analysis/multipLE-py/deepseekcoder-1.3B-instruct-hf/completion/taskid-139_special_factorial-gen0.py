def special_factorial(n: int) -> int:
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    """

    # write your code here
    def factorial(n: int) -> int:
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)

    result = 1
    for i in range(1, n + 1):
        result *= factorial(i)
    return result
