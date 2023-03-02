/**
 * @param {number} n
 * @return {number}
 */
var countPrimes = function(n) {
    //Given an integer n, return the number of prime numbers that are strictly less than n.

    //sieve of eratosthenes

    //create an array of all numbers from 2 to n
    //set all numbers to true except 2 and 3, which are prime.
    //for each number in the array, if it is true, then set all multiples of
    //to false.
    //count the number of true values in the array.
    //return the number of true values.
    let primes = [2,3];
    let count = 2
    for(let i = 4; i < n; i++){
        let isPrime = true;
        for(let j = 0; j < primes.length; j++){
            if(i % primes[j] === 0){
                isPrime = false;
                break;
            }
        }
        if(isPrime){
            primes.push(i);
            count++;
        }
    }
    return count;
}
