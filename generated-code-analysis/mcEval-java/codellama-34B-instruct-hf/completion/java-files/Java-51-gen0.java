import java.util.HashMap;

class Problem {

  /**
   * Calculate the sum of unique elements in the given integer array.
   *
   * @param nums An array of integers.
   * @return The sum of unique elements.
   *
   * Example:
   * calculateUniqueSum(new int[]{1, 2, 3, 2})
   * Output: 4
   */
  public static int calculateUniqueSum(int[] nums)  {
    HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();

    for (int i : nums) {
      if (!map.containsKey(i)) {
        map.put(i, 1);
      }
    }

    int sum = 0;
    for (int key : map.keySet()) {
      sum += key;
    }

    return sum;
  }
  public static void main(String[] args) {
    assert calculateUniqueSum(new int[] { 1, 4, 5, 1, 2, 4 }) == 7; // Test Case 1
    assert calculateUniqueSum(new int[] { 0, 0, 0, 0 }) == 0; // Test Case 2
    assert calculateUniqueSum(new int[] { -1, -2, -3, -2 }) == -4; // Test Case 3

    System.out.println("All tests passed");
  }
}