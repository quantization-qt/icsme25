import java.util.ArrayList;
import java.util.List;

class Problem {

  /**
   * Find all stepping numbers in the range [low, high] where a stepping number is defined as a number where each digit is either one more or one less than the adjacent digit.
   *
   * @param low The lower bound of the range.
   * @param high The upper bound of the range.
   * @return A list of stepping numbers within the range [low, high] sorted in ascending order.
   *
   * Example:
   * findSteppingNumbers(0, 21)
   * Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 21]
   */
  public static List<Integer> findSteppingNumbers(int low, int high)  {
    // Create a list to store the result
    List<Integer> result = new ArrayList<>();

    // If the low is greater than 9, start from low, otherwise start from 0
    for(int curr = 0; curr <= 9; curr++){
      if(curr >= low) result.add(curr);
      dfs(curr, low, high, result);
    }

    return result;
  }
  public static void main(String[] args) {
    assert findSteppingNumbers(0, 21)
      .equals(
        new ArrayList<>(List.of(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 21))
      );
    assert findSteppingNumbers(10, 15).equals(new ArrayList<>(List.of(10, 12)));
    assert findSteppingNumbers(50, 55).equals(List.of(54));

    System.out.println("All tests passed");
  }
}
