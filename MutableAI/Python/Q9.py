class Solution(object):
        #You are given a string s. You can convert s to a palindrome by adding characters in front of it.
        #constraints: 0 <= s.length <= 5 * 104 and s consists of lowercase English letters only.

    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        #if s is a palindrome, return s
        if s == s[::-1]:
            return s
        #find the longest palindrome suffix of s
        suffix = self.longestPalindromeSuffix(s)
        #return the concatenation of the suffix and the reverse of the suffix
        return suffix + s[len(suffix):][::-1]
        
   