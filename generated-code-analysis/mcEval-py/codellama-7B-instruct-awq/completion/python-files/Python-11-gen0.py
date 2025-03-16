def cantor_numbering(N: int) -> str:
    """
    Determines the numerator and denominator of the N-th term in the Cantor table.

    Args:
    - N (int): The position in the Cantor table to find the corresponding fraction for.

    Returns:
    - str: A string representation of the fraction at the N-th position in the Cantor table.
    """
    # Set up the numerator and denominator.
    numerator = 1
    denominator = 1

    # Keep track of the numerator and denominator.
    numerator_previous = 1
    denominator_previous = 1

    # Iterate until we find the N-th term.
    for i in range(N):
        numerator, denominator = denominator, numerator + denominator
        numerator_previous, denominator_previous = numerator, denominator

    # Add the final fraction to our list.
    numerator, denominator = denominator, numerator + denominator

    # Return the string representation of the fraction.
    return f"{numerator}/{denominator}"
def test_cantor_numbering():
    # Test case 1: N = 1, the first element, should be "1/1"
    assert cantor_numbering(1)=="1/1"

    # Test case 2: N = 2, the second element, should be "1/2"
    assert cantor_numbering(2)=="1/2"

    # Test case 3: N = 6, the sixth element, should be "1/3"
    assert cantor_numbering(6)=="1/3"

    # Corrected test case: N = 7, the seventh element, should be "1/4"
    assert cantor_numbering(7) == "1/4"

    # Additional test case: N = 8, the eighth element, should be "2/3"
    assert cantor_numbering(8) == "2/3"


test_cantor_numbering()