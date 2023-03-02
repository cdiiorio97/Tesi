package Java;

public class Q6 {
    public int lengthOfLongestSubstring(String s) {
        /*Given a string s, find the length of the longest substring
        *without repeating characters. 
        */
        int max = 0;
        int start = 0;
        int end = 0;
        int count = 0;
        int[] charCount = new int[256];
        while (end < s.length()) {
            if (charCount[s.charAt(end)] == 0) {
                charCount[s.charAt(end)]++;
                end++;
                count++;
            } else {
                charCount[s.charAt(end)]++;
                end++;
                count++;
                while (charCount[s.charAt(start)] > 1) {
                    charCount[s.charAt(start)]--;
                    start++;
                    count--;
                }
            }
            if (count > max) {
                max = count;
            }
        }
        return max;
    }
}