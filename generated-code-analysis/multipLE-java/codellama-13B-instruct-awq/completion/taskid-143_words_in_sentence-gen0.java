import java.util.*;
import java.lang.reflect.*;
import org.javatuples.*;
import java.security.*;
import java.math.*;
import java.io.*;
import java.util.stream.*;
class Problem {
    // You are given a string representing a sentence,
    // the sentence contains some words separated by a space,
    // and you have to return a string that contains the words from the original sentence,
    // whose lengths are prime numbers,
    // the order of the words in the new string should be the same as the original one.
    // Example 1:
    // >>> wordsInSentence(("This is a test"))
    // ("is")
    // Example 2:
    // >>> wordsInSentence(("lets go for swimming"))
    // ("go for")
    // Constraints:
    // * 1 <= len(sentence) <= 100
    // * sentence contains only letters
    public static String wordsInSentence(String sentence) {

        String [] words = sentence.split(" ");
        StringBuilder primeString = new StringBuilder();
        for (int i = 0; i < words.length; i++) {
            if (isPrime(words[i].length())) {
                primeString.append(words[i]).append(" ");
            }
        }
        return primeString.toString().trim();
    }
    public static void main(String[] args) {
    assert(wordsInSentence(("This is a test")).equals(("is")));
    assert(wordsInSentence(("lets go for swimming")).equals(("go for")));
    assert(wordsInSentence(("there is no place available here")).equals(("there is no place")));
    assert(wordsInSentence(("Hi I am Hussein")).equals(("Hi am Hussein")));
    assert(wordsInSentence(("go for it")).equals(("go for it")));
    assert(wordsInSentence(("here")).equals(("")));
    assert(wordsInSentence(("here is")).equals(("is")));
    }

}
