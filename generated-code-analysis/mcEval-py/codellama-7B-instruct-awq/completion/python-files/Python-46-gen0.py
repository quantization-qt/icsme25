def minimum_students_to_leave(heights):
    """
    Calculate the minimum number of students that need to leave to form a choir formation.
    A choir formation is defined such that for some position 'i', the heights of students
    increase from the start to 'i' and decrease from 'i' to the end of the formation.

    Args:
    heights (List[int]): A list of student heights.

    Returns:
    int: The minimum number of students that need to leave.
    """
    left_student_heights = []
    right_student_heights = []

    for i in range(len(heights)):
        left_student_heights.append(heights[i])
        if i + 1 < len(heights):
            right_student_heights.append(heights[i + 1])

    min_left = min(left_student_heights)
    min_right = min(right_student_heights)

    if min_left < min_right:
        min_left_index = left_student_heights.index(min_left)
        min_left_height = left_student_heights[min_left_index]

        min_right_height = right_student_heights[right_student_heights.index(min_right)]
        return min_left_height - min_right_height
    else:
        min_right_index = right_student_heights.index(min_right)
        min_right_height = right_student_heights[min_right_index]

        min_left_height = left_student_heights[left_student_heights.index(min_left)]
        return min_left_height - min_right_height
def test_minimum_students_to_leave():
    # Test case 1: Provided example
    assert minimum_students_to_leave([186, 186, 150, 200, 160, 130, 197, 220]) == 4, "Test case 1 failed"

    # Test case 2: All students have the same height
    assert minimum_students_to_leave([150, 150, 150, 150, 150]) == 4, "Test case 2 failed"

    # Test case 3: Students are already in a choir formation
    assert minimum_students_to_leave([130, 150, 170, 190, 170, 150, 130]) == 0, "Test case 3 failed"

    # Test case 4: Students are in strictly increasing order
    assert minimum_students_to_leave([130, 135, 140, 145, 150, 155]) == 0, "Test case 4 failed"

    # Test case 5: Students are in strictly decreasing order
    assert minimum_students_to_leave([155, 150, 145, 140, 135, 130]) == 0, "Test case 5 failed"

    # Test case 6: Optimal choir formation is not including the first or last student
    assert minimum_students_to_leave([200, 180, 190, 170, 210, 160, 220]) == 3, "Test case 6 failed"

    print("All test cases passed!")

# Run the test function
test_minimum_students_to_leave()