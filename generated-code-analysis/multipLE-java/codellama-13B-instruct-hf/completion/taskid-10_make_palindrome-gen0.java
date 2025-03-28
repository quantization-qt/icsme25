import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Find the shortest palindrome that begins with a supplied string.
    // Algorithm idea is simple:
    // - Find the longest postfix of supplied string that is a palindrome.
    // - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    // >>> makePalindrome((""))
    // ("")
    // >>> makePalindrome(("cat"))
    // ("catac")
    // >>> makePalindrome(("cata"))
    // ("catac")
    public static String makePalindrome(String string) {

        String palindrome = "";
        // Reversed string for checking palindromicity.
        String stringReversed = "";
        // Get the length of the string.
        int stringLength = string.length();
        // Get the reverse of the string.
        for (int i = 0; i < stringLength; i++) {
            stringReversed = (stringReversed + string.charAt(stringLength - i - 1));
        }
        // Get the length of the reversed string.
        int stringReversedLength = stringReversed.length();
        // Check if the reversed string is a prefix of the original string.
        for (int i = 0; i < stringReversedLength; i++) {
            if (stringReversed.equals(string.substring(0, i + 1))) {
                palindrome = (string + stringReversed.substring(i + 1));
                break;
            }
        }
        return palindrome;
    }
    public static void main(String[] args) {
    assert(makePalindrome(("")).equals(("")));
    assert(makePalindrome(("x")).equals(("x")));
    assert(makePalindrome(("xyz")).equals(("xyzyx")));
    assert(makePalindrome(("xyx")).equals(("xyx")));
    assert(makePalindrome(("jerry")).equals(("jerryrrej")));
    }

}
