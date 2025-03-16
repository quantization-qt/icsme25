from itertools import permutations

def find_number_combinations():
    """
    Generate all unique combinations of three numbers, each formed from the digits 1 to 9 without repetition,
    such that the second number is twice the first and the third is three times the first.

    Returns:
        list of tuples: A sorted list of tuples, where each tuple contains three integers representing the
                        valid number combinations in ascending order based on the first number.

    Example:
        >>> find_number_combinations()
        [(123, 246, 369), (124, 248, 372), ...]
    """
    valid_combinations = []

    # Generate all unique permutations of numbers from 1 to 9
    for permutation in permutations(range(1, 10)):

        # Select first number
        first_number = permutation[0] * 100 + permutation[1] * 10 + permutation[2]

        # Select second number
        second_number = permutation[3] * 100 + permutation[4] * 10 + permutation[5]

        # Select third number
        third_number = permutation[6] * 100 + permutation[7] * 10 + permutation[8]

        # If second number is twice the first number and third number is three times the first number
        if second_number == 2 * first_number and third_number == 3 * first_number:

            # Add combination to list
            valid_combinations.append((first_number, second_number, third_number))

    # Return list of valid combinations sorted in ascending order based on first number
    return sorted(valid_combinations)
def test_find_number_combinations():
    # Call the function to get the combinations
    combinations = find_number_combinations()

    # Check that we have at least one valid combination
    assert len(combinations) > 0, "There should be at least one valid combination."

    # Iterate over each combination to perform further checks
    for combo in combinations:
        # Each combination should have exactly three numbers
        assert len(combo) == 3, "Each combination should have three numbers."

        # Check if numbers are 3-digit numbers
        for num in combo:
            assert 100 <= num <= 999, f"Each number should be a 3-digit number, got {num}."

        # Check the 1:2:3 ratio
        assert combo[1] == 2 * combo[0] and combo[2] == 3 * combo[0], "The numbers should be in a 1:2:3 ratio."

    print("All test cases passed!")

# Run the test cases
test_find_number_combinations()