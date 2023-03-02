class Solution(object):
    def romanToInt(self, s):
        #Given a roman numeral, convert it to an integer.

        """
        :type s: str
        :rtype: int
        """

        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        roman_num = 0

        for i in range(len(s)):

            if s[i] in roman_dict:
                roman_num += roman_dict[s[i]]
            else:
                roman_num += roman_dict[s[i]] * 10

        return
    