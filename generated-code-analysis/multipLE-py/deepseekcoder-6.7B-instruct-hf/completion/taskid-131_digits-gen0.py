def digits(n: int) -> int:
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    >>> digits(1)
    1
    >>> digits(4)
    0
    >>> digits(235)
    15
    """

    product = 1
    has_odd_digit = False
    for digit in str(n):
        digit = int(digit)
        if digit % 2 == 1:
            product *= digit
            has_odd_digit = True
    return product if has_odd_digit else 0
