import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Given a positive integer n, return a pair that has the number of even and odd
    // integer palindromes that fall within the range(1, n), inclusive.
    // Example 1:
    // >>> evenOddPalindrome((3l))
    // (Pair.with(1l, 2l))
    // Explanation:
    // Integer palindrome are 1, 2, 3. one of them is even, and two of them are odd.
    // Example 2:
    // >>> evenOddPalindrome((12l))
    // (Pair.with(4l, 6l))
    // Explanation:
    // Integer palindrome are 1, 2, 3, 4, 5, 6, 7, 8, 9, 11. four of them are even, and 6 of them are odd.
    // Note:
    // 1. 1 <= n <= 10^3
    // 2. returned pair has the number of even and odd integer palindromes respectively.
    public static Pair<Long, Long> evenOddPalindrome(long n) {

        long evens = 0, odds = 0;
        if (n <= 2) {
            evens = n;
            odds = n;
        } else {
            long k = 10;
            long temp = n;
            while (temp > 0) {
                odds += 9 * k;
                temp = temp - k;
                k *= 10;
            }
            temp = n;
            while (temp > 0) {
                evens += (temp % 10) * k;
                temp = temp - k;
                k *= 10;
            }
            odds += evens;
            evens -= 1;
        }
        return Pair.with(evens, odds);
    }
    public static void main(String[] args) {
    assert(evenOddPalindrome((123l)).equals((Pair.with(8l, 13l))));
    assert(evenOddPalindrome((12l)).equals((Pair.with(4l, 6l))));
    assert(evenOddPalindrome((3l)).equals((Pair.with(1l, 2l))));
    assert(evenOddPalindrome((63l)).equals((Pair.with(6l, 8l))));
    assert(evenOddPalindrome((25l)).equals((Pair.with(5l, 6l))));
    assert(evenOddPalindrome((19l)).equals((Pair.with(4l, 6l))));
    assert(evenOddPalindrome((9l)).equals((Pair.with(4l, 5l))));
    assert(evenOddPalindrome((1l)).equals((Pair.with(0l, 1l))));
    }

}
