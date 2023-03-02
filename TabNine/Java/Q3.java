package Java;

public class Q3 {
    public int reverseBits(int n) {
        //Reverse bits of a given 32 bits unsigned integer.
        int rev = 0;
        for (int i = 0; i < 32; i++) {
            rev = rev << 1 | (n & 1);
            n = n >> 1;
        }
        return rev;
    }
}
