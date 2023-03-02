/**
 * @param {number} n
 * @return {number}
 */
var countPrimes = function(n) {
    //Given an integer n, return the number of prime numbers that are strictly less than n.

    //Example 1:
    //Input: n = 10
    //Output: 4
    //Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

    //Example 2:
    //Input: n = 0
    //Output: 0

    //Example 3:
    //Input: n = 1
    //Output: 0

    //Constraints:
    //0 <= n <= 5 * 106

    //SOLUTION 13
    let count = 0;
    let isPrime = new Array(n).fill(true);
    for (let i = 2; i < n; i++) {
        if (isPrime[i]) {
            count++;
            for (let j = i * i; j < n; j += i) {
                isPrime[j] = false;
            }
        }
    }
    return count;


};