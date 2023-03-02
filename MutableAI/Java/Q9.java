package Java;

public class Q9 {
    /*You are given a string s. You can convert s to a palindrome by adding characters in front of it.
    Return the shortest palindrome you can find by performing this transformation. */

    public String shortestPalindrome(String s) {
        if (s.length() == 0) return "";
        StringBuilder sb = new StringBuilder(s);
        sb.reverse();
        String rev = sb.toString();
        StringBuilder sb2 = new StringBuilder(s);
        sb2.append("$").append(rev);
        String str = sb2.toString();
        int[] dp = new int[str.length()];
        int i = 0;
        int j = 0;
        while (i < str.length()) {
            if (str.charAt(i) == str.charAt(j)) {
                dp[i] = j + 1;
                i++;
                j++;
            } else if (j > 0) {
                j = dp[j - 1];
            } else {
                i++;
            }
        }
        return rev.substring(0, s.length() - dp[str
}
