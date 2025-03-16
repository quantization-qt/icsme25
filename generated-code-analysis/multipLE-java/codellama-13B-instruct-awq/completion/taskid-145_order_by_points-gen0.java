import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Write a function which sorts the given array list of integers
    // in ascending order according to the sum of their digits.
    // Note: if there are several items with similar sum of their digits,
    // order them based on their index in original array list.
    // For example:
    // >>> orderByPoints((new ArrayList<Long>(Arrays.asList((long)1l, (long)11l, (long)-1l, (long)-11l, (long)-12l))))
    // (new ArrayList<Long>(Arrays.asList((long)-1l, (long)-11l, (long)1l, (long)-12l, (long)11l)))
    // >>> orderByPoints((new ArrayList<Long>(Arrays.asList())))
    // (new ArrayList<Long>(Arrays.asList()))
    public static ArrayList<Long> orderByPoints(ArrayList<Long> nums) {

        ArrayList<Long> ans = new ArrayList<>();
        int n = nums.size();
        for (long num : nums) {
            int sum = 0;
            while (num > 0) {
                sum += (int)(num % 10);
                num /= 10;
            }
            ans.add(num);
        }
        Collections.sort(ans, (a, b) -> {
            int sum1 = 0;
            int sum2 = 0;
            while (a > 0) {
                sum1 += (int)(a % 10);
                a /= 10;
            }
            while (b > 0) {
                sum2 += (int)(b % 10);
                b /= 10;
            }
            if (sum1 == sum2) {
                return nums.indexOf(a) - nums.indexOf(b);
            }
            return sum1 - sum2;
        });
        return ans;
    }
    public static void main(String[] args) {
    assert(orderByPoints((new ArrayList<Long>(Arrays.asList((long)1l, (long)11l, (long)-1l, (long)-11l, (long)-12l)))).equals((new ArrayList<Long>(Arrays.asList((long)-1l, (long)-11l, (long)1l, (long)-12l, (long)11l)))));
    assert(orderByPoints((new ArrayList<Long>(Arrays.asList((long)1234l, (long)423l, (long)463l, (long)145l, (long)2l, (long)423l, (long)423l, (long)53l, (long)6l, (long)37l, (long)3457l, (long)3l, (long)56l, (long)0l, (long)46l)))).equals((new ArrayList<Long>(Arrays.asList((long)0l, (long)2l, (long)3l, (long)6l, (long)53l, (long)423l, (long)423l, (long)423l, (long)1234l, (long)145l, (long)37l, (long)46l, (long)56l, (long)463l, (long)3457l)))));
    assert(orderByPoints((new ArrayList<Long>(Arrays.asList()))).equals((new ArrayList<Long>(Arrays.asList()))));
    assert(orderByPoints((new ArrayList<Long>(Arrays.asList((long)1l, (long)-11l, (long)-32l, (long)43l, (long)54l, (long)-98l, (long)2l, (long)-3l)))).equals((new ArrayList<Long>(Arrays.asList((long)-3l, (long)-32l, (long)-98l, (long)-11l, (long)1l, (long)2l, (long)43l, (long)54l)))));
    assert(orderByPoints((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l, (long)4l, (long)5l, (long)6l, (long)7l, (long)8l, (long)9l, (long)10l, (long)11l)))).equals((new ArrayList<Long>(Arrays.asList((long)1l, (long)10l, (long)2l, (long)11l, (long)3l, (long)4l, (long)5l, (long)6l, (long)7l, (long)8l, (long)9l)))));
    assert(orderByPoints((new ArrayList<Long>(Arrays.asList((long)0l, (long)6l, (long)6l, (long)-76l, (long)-21l, (long)23l, (long)4l)))).equals((new ArrayList<Long>(Arrays.asList((long)-76l, (long)-21l, (long)0l, (long)4l, (long)23l, (long)6l, (long)6l)))));
    }

}
