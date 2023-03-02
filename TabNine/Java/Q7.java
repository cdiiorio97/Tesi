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

    private boolean isPrime(int i) {
        return false;
    }
}
