import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // brackets is a string of "<" and ">".
    // return true if every opening bracket has a corresponding closing bracket.
    // >>> correctBracketing(("<"))
    // (false)
    // >>> correctBracketing(("<>"))
    // (true)
    // >>> correctBracketing(("<<><>>"))
    // (true)
    // >>> correctBracketing(("><<>"))
    // (false)
    public static boolean correctBracketing(String brackets) {

        char[] array = brackets.toCharArray();
        Stack<Character> stack = new Stack();
        for (char c : array) {
            if (c == '<') {
                stack.push(c);
            } else {
                if (!stack.isEmpty()) {
                    stack.pop();
                } else {
                    return false;
                }
            }
        }
        return stack.isEmpty();
    }
    public static void main(String[] args) {
    assert(correctBracketing(("<>")) == (true));
    assert(correctBracketing(("<<><>>")) == (true));
    assert(correctBracketing(("<><><<><>><>")) == (true));
    assert(correctBracketing(("<><><<<><><>><>><<><><<>>>")) == (true));
    assert(correctBracketing(("<<<><>>>>")) == (false));
    assert(correctBracketing(("><<>")) == (false));
    assert(correctBracketing(("<")) == (false));
    assert(correctBracketing(("<<<<")) == (false));
    assert(correctBracketing((">")) == (false));
    assert(correctBracketing(("<<>")) == (false));
    assert(correctBracketing(("<><><<><>><>><<>")) == (false));
    assert(correctBracketing(("<><><<><>><>>><>")) == (false));
    }

}
