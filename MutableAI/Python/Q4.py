class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        #Given a roman numeral, convert it to an integer.
        #Input is guaranteed to be within the range from 1 to 3999.
        #Example :
        #Input : "XIV"
        #Output : 14
        #Input : "XIX"
        #Output : 19
       
        #Solution:
        #1. Create a dictionary with the roman numeral as key
        #2. Iterate through the string and add the value of the roman numeral to
        #3. Return the sum of the dictionary
        #4. If the roman numeral is not in the dictionary, return 0
        #5. If the roman numeral is in the dictionary, return the value of the
       

        roman_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        sum = 0
        for i in range(len(s)):
            if i == len(s)-1:
                sum += roman_dict[s[i]]
            else:
                if roman_dict[s[i]] >= roman_dict[s[i+1]]:
                    sum += roman_dict[s[i]]
                else:
                    sum -= roman_dict[s[i]]
        return sum
    