package Java;

public class Q7 {
    public int countPrimes(int n) {
        //Given an integer n, return the number of prime numbers 
        //that are strictly less than n. with 0 <= n <= 5 * 106
    
    
    /* In questo primo caso, il programma non funziona perchè non è stato implementato il metodo isPrime
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
    }*/



    /*2° tentativo, il codice eseguiva correttamente i test ma andava contro a time limit exceeded
        int count = 0;
        for (int i = 2; i < n; i++) {
            if (isPrime(i)) {
                count++;
            }
        }
        return count;
    }
    public boolean isPrime(int n) {
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
     */
    

      //Esecuzione corretta, 3° tentativo
        boolean[] isPrime = new boolean[n];
        for (int i = 2; i < n; i++) {
            isPrime[i] = true;
        }
        for (int i = 2; i * i < n; i++) {
            if (!isPrime[i]) {
                continue;
            }
            for (int j = i * i; j < n; j += i) {
                isPrime[j] = false;
            }
        }
        int count = 0;
        for (int i = 2; i < n; i++) {
            if (isPrime[i]) {
                count++;
            }
        }
        return count;
        
    }
    

    
}

