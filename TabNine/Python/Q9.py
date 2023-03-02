class Solution(object):
        #You are given a string s. You can convert s to a palindrome by adding characters in front of it.
        #constraints: 0 <= s.length <= 5 * 104 and s consists of lowercase English letters only.

    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        if not s:
             return ""
        
        if len(s) == 1:
            return s
        
        if len(s) == 2:
            if s[0] == s[1]:
                return s[0]
            else:
                return ""
            
    