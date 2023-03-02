/**
 * @param {number} n
 * @return {number}
 */
var countPrimes = function(n) {
    //Given an integer n, return the number of prime numbers that are strictly less than n.
    //constraint: 0 <= n <= 5 * 10^6


    if(n <= 1) return 0;

    let count = 0;

    for(let i = 2; i < n; i++){

        if(isPrime(i)){
            count++;
        }
    }

    return count

    function isPrime(n) {
        if(n <= 1) return false;

        for(let i = 2; i < n; i++){
            if(n % i === 0) return false;
        }

        return true;
    }
}