def fib4(n: int) -> int:
    """The Fib4 number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    Please write a function to efficiently compute the n-th element of the fib4 number sequence.  Do not use recursion.
    >>> fib4(5)
    4
    >>> fib4(6)
    8
    >>> fib4(7)
    14
    """

    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 2
    if n == 3:
        return 0
    fib_4_minus_1, fib_4_minus_2, fib_4_minus_3, fib_4_minus_4 = 0, 0, 2, 0
    for _ in range(n - 3):
        fib_4 = fib_4_minus_1 + fib_4_minus_2 + fib_4_minus_3 + fib_4_minus_4
        fib_4_minus_4 = fib_4_minus_3
        fib_4_minus_3 = fib_4_minus_2
        fib_4_minus_2 = fib_4_minus_1
        fib_4_minus_1 = fib_4
    return fib_4_minus_1 + fib_4_minus_2 + fib_4_minus_3 + fib_4_minus_4
