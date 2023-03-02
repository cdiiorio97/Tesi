package Java;

public class Q7 {
    public int countPrimes(int n) {
        //Given an integer n, return the number of prime numbers 
        //that are strictly less than n. with 0 <= n <= 5 * 106
        
        int count = 0;
        for (int i = 2; i < n; i++) {
            if (isPrime(i)) {
                count++;
            }
        }
        return count;
    }
    
    public boolean isPrime(int n) {
        //check if n
        if (n <= 1) {
            return false;
        } else if (n <= 3) {
            return true;
        } else if (n % 2 == 0 || n % 3 == 0) {
            return false;
        } else {
            for (int i = 5; i * i <= n; i += 6) {
                if (n % i == 0 || n % (i + 2) == 0) {
                    return false;
                }
            }
            return true;
        }
    }
}
