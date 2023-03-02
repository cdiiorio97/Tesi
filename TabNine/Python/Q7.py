class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Given an integer n, return the number of prime numbers that are strictly less than n.
        # The number of prime numbers less than 10 is 4, they are 2, 3, 5, 7.
        # The number of prime numbers less than 100 is 25, they are 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97.

        def isPrime(n):
             if n <= 1:
                return False
             if n == 2:
                return True
             if n % 2 == 0:
                return False
             for i in range(3, int(math.sqrt(n))+1, 2):
                if n % i == 0:
                    return False
             return True
        
        count = 0

        for i in range(2, int(math.sqrt(n))+1):

            if isPrime(i):
                count += 1

        return
    