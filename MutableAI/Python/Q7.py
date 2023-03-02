class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Given an integer n, return the number of prime numbers that are strictly less than n.
        # The number of prime numbers less than 10 is 4, they are 2, 3, 5, 7.
        # The number of prime numbers less than 100 is 25, they are 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97.

        # Example:
        # Input: 10
        # Output: 4
        # Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7
        # Example:
        # Input: 100
        # Output: 25
        # Explanation: There are 25 prime numbers less than 100, they are 2, 3, 5, 7, 11, 13, 17, 19, 23

        # Note:
        # 1. 0 and 1 are not prime numbers.
        # 2. If n is smaller than 2, return 0.
        # 3. The n will not exceed 100,000,000. (1e8)
        # 4. The n is a 32-bit signed integer, which means the length of the
        # 5. The following code should be used to get the result.
        # 6. The time complexity should be less than O(n ^ 2).
        # 7. The space complexity should be less than O(n).
        

        # Solution 1:
        # Time: O(n)
        # Space: O(n)
        # if n < 2:
        #     return 0
        # primes = [
            # True for _ in range(n)  # initialize the array with all True values.
            # ]  # primes[0] and primes[1] are not prime numbers
            # primes[0] = primes[1] = False  # 0 and 1
            # for i in range(2, int(n ** 0.5) + 1):

                # if primes[i]:  # if i is prime number, then check all the

                    # for j in range(i * i, n, i):  # mark all the

                        # primes[j] = False  # which are multiples of i.
                        # print(j)  # for testing purpose.
                        # print(primes)  # for testing purpose.
                        # print("\n")  # for testing purpose.
                        # print(i)  # for testing purpose.
                        
            # return sum(primes[:n])  # return the number of prime numbers less
            # than n.

            # Solution 2:
            # Time: O(n)
            # Space: O(1)
            # if n < 2:
            #     return 0  # 0 and 1 are not prime numbers.
            # count = 0  # count the number of prime numbers less than n.
            # for i in range(2, n):  # check all the numbers less than n

                # if i == 2 or i == 3 or i == 5 or i == 7:  # 2, 3, 5, 7 are prime numbers.

                    # count += 1  # count the number of prime numbers less than n.
                    # continue  # continue to the next number.
                    # if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0:  # if i is not prime number, then continue to
                    #     continue  # the next number.
                    # count += 1  # count the number of prime numbers less than n.
                    #
                    # print(i)  # for testing purpose.
                    # print(count)  # for testing purpose.
                    # print("\n")  # for testing purpose.
                   
        
            return count  # return the number of prime numbers less than n.
            # Solution 3:
            # Time: O(n)
            # Space: O(1)
            # if n < 2:
            #     return 0  # 0 and 1 are not prime numbers.
            # count = 0  # count the number of prime numbers less than n.
            # for i in range(2, n):  # check all the numbers less than
                # if i == 2 or i == 3 or i == 5 or i == 7:  # 2, 3, 5, 7 are prime numbers.
                    # count += 1  # count the number of prime numbers less than n.
                    # continue  # continue to the next number.
                    # if i % 2 == 0 or
                    # i % 3 == 0 or
                    # i % 5 == 0 or i % 7 == 0:  # if i is not
                    #     continue  # prime number, then continue to the next number.
                    # count += 1  # count the number of prime numbers less than n.
                    #
                    # print(i)  # for testing purpose.
                    # print(count
                    # print("\n")  # for testing purpose.
                    #
                    # return count  # return the number of prime numbers less than n.


            # Solution 4:
            # Time: O(n)
            # Space: O(1)
            # if n < 2:
            #     return 0  #  
            # count = 0  # count the number of prime numbers less than n.
            # for i in range(2, n):  # check all the numbers less than n.
                # if i == 2 or i == 3 or i == 5 or i == 7:  # 2, 3, 5, 7 are prime numbers.
                    # count += 1
                    # continue  # continue to the next number.
                    # if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0:  # if i is not prime number, then continue to
                    #     continue  # the next number.


                    # count += 1  # count the number of prime numbers less than n.
                    # print(i)  # for testing purpose.
                    # print(count)  #

                    # return count  # return the number of prime numbers less than n.
                    #
                    #
                    #

                    # Solution 5:
                    # Time: O(n) '
                    # Space: O(1) '
                    # if n < 2:  #   '
                    #     return 0  #   '
                    # count = 0  # count the number of prime numbers less than n. '
                    # for i in range(2, n
                    # if i == 2 or i == 3 or i == 5 or i == 7:  # 2, 3, 5, 7 are prime numbers. '
                    #     count += 1  # count the number of prime numbers less than n. '
                    #     continue  # continue to the next number. '
                    # if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0:  # if i is not prime number, then continue to
                    #     continue  # the next number. ' '
                    # count += 1  # count the number of prime numbers less than n. '
                    # print(i)  # for testing purpose. ' '
                    # print(count)  # ' '
                    # return count  # return the number of prime numbers less
                    # '
                    # '
                    # '
                    # '

        # Solution 6:
                    # Time: O(n) '
                    # Space: O(1) '
                    # if n < 2:  #   '
                    #     return 0  #   ' '
                    # count = 0  # count the number of prime numbers less than n. ' ' '
                    # for i in range(2, n + 1):  #   ' ' '
                        # if i == 2 or i == 3 or i == 5 or i == 7:  # 2, 3, 5, 7 are prime numbers. ' ' ' '
                        #
                        # count += 1  # count the number of prime numbers less than n. ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' '
                        # continue  # continue to the next number. ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' '
                        # if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0:  # if i is not prime number, then continue to
                        #     continue  # the next number. ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' '
                        # count += 1  # count the number of prime numbers less than n. ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' '
                        # print(i)  # for testing purpose. ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' '
                        # print(count)  # ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' '
                        # return count  # return the number of prime numbers less than n. ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' '
                        # ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' '
                        # ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' '
                        # ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' '


                        