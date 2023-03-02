class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #Given a string s, find the length of the longest substring without repeating characters.
        
        #Example:
        #Given s = "abcabcbb", the answer is "abc
        #Given s = "bbbbb", the answer is "b"
        #Given s = "pwwkew", the answer is "wke"
        
        #The longest substring without repeating characters is "wke", with the length of 3.
        #Note:
        #The string contains only lowercase letters.

        #O(n) space complexity
        #O(n) time complexity

        #The idea is to use a hashmap to store the characters and their last index.
        #Then, we can use two pointers to scan the string. The first pointer is to scan
        #the string from left to right, the second pointer is to scan the string from right to
        #left. Whenever we find a character that is already in the hashmap, we update the
        #to the index of the character plus one. This is because we want to make sure that
        #the character is not repeated. Moreover, we also need to make sure that the character is
        #not repeated in the substring that we have already scanned.

        #The time complexity is O(n). The space complexity is O(n).
        #The time complexity is O(n). The space complexity is O(n).
        #The time complexity is O(n). The space complexity is O(n).

        #The time complexity is O(n). The space complexity is O(n).

        #The time complexity is O(n). The space complexity is O(n).
        #The time complexity is O(n). The space complexity is O(n).
        #The time complexity is O(n). The space complexity is O(n).
