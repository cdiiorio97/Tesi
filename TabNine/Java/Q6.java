package Java;

public class Q6 {
    public int lengthOfLongestSubstring(String s) {
        /*Given a string s, find the length of the longest substring
        *without repeating characters. 
        */

        if(s == null || s.length() == 0){
            return 0;
        }
        int max = 0;
        int start = 0;
        int end = 0;
        char[] arr = s.toCharArray();
        while(end < arr.length){
            if(arr[end]!= arr[start]){
                max = Math.max(max, end - start + 1);
                start++;
            }
            end++;
        }
        return max;
    }
}
