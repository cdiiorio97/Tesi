class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #Given a string s, find the length of the longest substring without repeating characters.
        
        if not s:
            return 0
        
        max_len = 0

        for i in range(len(s)):

            if s[i] not in s[i+1:]:
                max_len = max(max_len, i-i+1)

        return