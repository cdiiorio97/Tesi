class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        #Reverse bits of a given 32 bits unsigned integer.
        #Example:
        #Input: 00000010100101000001111010011100
        #Output: 0011100101111000001010010100000
        #Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 0011100101111000001010010100000.
        #Note:
        #Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
        #For example, given input 43261596, your function should return 964176192.
        n = n ^ (n >> 31)
        n = n ^ (n >> 1)
        n = n ^ (n >> 2)
        n = n ^ (n >> 4)
        n = n ^ (n >> 8)
        n = n ^ (n >> 16)
        return n
    