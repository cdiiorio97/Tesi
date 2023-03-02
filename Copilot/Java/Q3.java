package Java;

public class Q3 {
    public int reverseBits(int n) {
        //Reverse bits of a given 32 bits unsigned integer.

        int result = 0;
        for (int i = 0; i < 32; i++) {
            result = result << 1;
            result = result | (n & 1);
            n = n >> 1;
        }
        return result;
    
    }
    
}
