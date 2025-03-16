import java.util.*;

class Problem {
    /**
     * Given an integer k, return the minimum number of Fibonacci numbers whose sum is equal to k.
     * Fibonacci numbers are defined as follows:
     * F1 = 1
     * F2 = 1
     * Fn = Fn-1 + Fn-2, for n > 2.
     * It is guaranteed that there is at least one valid solution for the given k.
     *
     * Example 1:
     * Input: k = 7
     * Output: 2
     * Explanation: Fibonacci numbers are: 1, 1, 2, 3, 5, 8, 13, ...
     * For k = 7, we can get 2 + 5 = 7.
     *
     * Example 2:
     * Input: k = 10
     * Output: 2
     * Explanation: For k = 10, we can get 2 + 8 = 10.
     *
     * Example 3:
     * Input: k = 19
     * Output: 3
     * Explanation: For k = 19, we can get 1 + 5 + 13 = 19.
     */
  public int findMinFibonacciNumbers(int k)  {
    int[] fib = new int[30];
    fib[0] = 1;
    fib[1] = 1;
    int i = 2;
    while (i < 30) {
      fib[i] = fib[i - 1] + fib[i - 2];
      i++;
    }
    List<Integer> fibs = new ArrayList<Integer>();
    for (int j = 0; j < 30; j++) {
      if (fib[j] > k) break;
      fibs.add(fib[j]);
    }
    int cnt = 0;
    for (int j = fibs.size() - 1; j >= 0; j--) {
      if (k == 0) break;
      if (k >= fibs.get(j)) {
        k = k - fibs.get(j);
        cnt++;
      }
    }
    return cnt;
  }
  public static void main(String[] args) {
    Problem solution = new Problem();

    // Test the function with different test cases
    assert solution.findMinFibonacciNumbers(7) == 2;
    assert solution.findMinFibonacciNumbers(10) == 2;
    assert solution.findMinFibonacciNumbers(13) == 1;
    System.out.println("All tests passed");
  }
}