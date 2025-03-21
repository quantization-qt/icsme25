import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    // For each of the group, output the deepest level of nesting of parentheses.
    // E.g. (()()) has maximum two levels of nesting while ((())) has three.
    // >>> parseNestedParens(("(()()) ((())) () ((())()())"))
    // (new ArrayList<Long>(Arrays.asList((long)2l, (long)3l, (long)1l, (long)3l)))
    public static ArrayList<Long> parseNestedParens(String paren_string) {

        // Create a Stack for keeping track of depth.
        Stack<String> stack = new Stack<>();
        String[] groups = paren_string.split(" ");
        ArrayList<Long> depths = new ArrayList<>();
        
        // Loop over groups.
        for(String group: groups) {
            long depth = 0;
            long maxDepth = 0;
            
            // Loop over chars in group.
            for(char ch: group.toCharArray()) {
                // Increase depth if char is '('
                if (ch == '(') {
                    depth++;
                    if (depth > maxDepth) {
                        maxDepth = depth;
                    }
                }
                // Decrease depth if char is ')'
                else if (ch == ')') {
                    depth--;
                }
            }
            // Add maxDepth to list.
            depths.add(maxDepth);
        }
        return depths;
    }
    public static void main(String[] args) {
    assert(parseNestedParens(("(()()) ((())) () ((())()())")).equals((new ArrayList<Long>(Arrays.asList((long)2l, (long)3l, (long)1l, (long)3l)))));
    assert(parseNestedParens(("() (()) ((())) (((())))")).equals((new ArrayList<Long>(Arrays.asList((long)1l, (long)2l, (long)3l, (long)4l)))));
    assert(parseNestedParens(("(()(())((())))")).equals((new ArrayList<Long>(Arrays.asList((long)4l)))));
    }

}
