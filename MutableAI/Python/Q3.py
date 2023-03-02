class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        #Reverse bits of a given 32 bits unsigned integer.
        #Example:
        #Input: 43261596
        #Output: 964176192
        #Explanation: 43261596 represented in binary as 0000001
        #             00001101 00001010 00000100 00001001, then the
        #             output is 964176192 represented in binary as 00111001 '
        #             00101100 00110010 00010100 00010001.
        #Follow up:
        #If this function is called many times, how would you optimize it?
        #Related problem: Reverse Integer.
        #Credits:Special thanks to @ts for adding this problem and creating all test cases.
        return int(bin(n)[2:].zfill(32)[::-1],2)
