package Java;

public class Q9 {
    public String shortestPalindrome(String s) {
    /*You are given a string s. You can convert s to a palindrome by adding characters in front of it.
    Return the shortest palindrome you can find by performing this transformation. */
    
        if(s == null || s.length() == 0)
        return s;
        
        int n = s.length();
        
        for(int i = 0; i < n; i++)

        {
            for(int j = i + 1; j < n; j++)
            {
                if(s.charAt(i) == s.charAt(j))
                {
                    return s.substring(i, j + 1);
                }
            }
        }
        
        return s;
    }
    public static void main(String[] args) {
        Q9 q = new Q9();
        System.out.println(q.shortestPalindrome("babad"));
    }      

}
