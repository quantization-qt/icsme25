import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Problem {

  /**
   * Given an integer n, return all the center symmetric numbers of length n.
   *
   * @param n The length of the center symmetric numbers.
   * @return A list of center symmetric numbers.
   *
   * Example:
   * centerSymmetricNumbers(2)
   * Output: ["11","69","88","96"]
   *
   * centerSymmetricNumbers(1)
   * Output: ["0","1","8"]
   */
  public static List<String> centerSymmetricNumbers(int n)  {
    if (n == 1) {
      return Arrays.asList("0", "1", "8");
    }

    List<String> result = new ArrayList<>();
    if (n % 2 == 0) {
      List<String> temp = centerSymmetricNumbers(n - 2);
      for (String s : temp) {
        result.add("0" + s + "0");
        result.add("1" + s + "1");
        result.add("6" + s + "9");
        result.add("8" + s + "8");
        result.add("9" + s + "6");
      }
    } else {
      List<String> temp = centerSymmetricNumbers(n - 2);
      for (String s : temp) {
        result.add("1" + s + "1");
        result.add("8" + s + "8");
        result.add("6" + s + "9");
        result.add("9" + s + "6");
      }
      result.add("0" + centerSymmetricNumbers(n - 2).get(0) + "0");
    }

    return result;
  }
  private static void assertArrays(String[] expected, List<String> actual) {
    if (actual == null || actual.size() != expected.length) {
      throw new AssertionError("Test case failed");
    }
    for (String str : expected) {
      if (!actual.contains(str)) {
        throw new AssertionError("Test case failed");
      }
    }
  }

  public static void main(String[] args) {
    assertArrays(
      new String[] { "11", "69", "88", "96" },
      centerSymmetricNumbers(2)
    );
    assertArrays(new String[] { "0", "1", "8" }, centerSymmetricNumbers(1));
    assertArrays(
      new String[] {
        "101",
        "111",
        "181",
        "609",
        "619",
        "689",
        "808",
        "818",
        "888",
        "906",
        "916",
        "986",
      },
      centerSymmetricNumbers(3)
    );
    System.out.println("All tests passed");
  }
}
