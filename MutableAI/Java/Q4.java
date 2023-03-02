package Java;

public class Q4 {
    public int romanToInt(String s) {
        //Given a roman numeral, convert it to an integer.
        //Input is guaranteed to be within the range from 1 to 3999.
        int sum = 0;
        int i = 0;
        while (i < s.length()) {
            char c = s.charAt(i);
            if (c == 'I') {
                sum += 1;
                i++;
            } else if (c == 'V') {
                sum += 5;
                i++;
            } else if (c == 'X') {
                sum += 10;
                i++;
            } else if (c == 'L') {
                sum += 50;
                i++;
            } else if (c == 'C') {
                sum += 100;
                i++;
            } else if (c == 'D') {
                sum += 500;
                i++;
            } else if (c == 'M') {
                sum += 1000;
                i++;
            } else if (c == 'I') {
                sum += 1;
                i++;
            }
           /* } else if (c == 'V') {
                sum += 5;
                i++;
            } else if (c == 'X') {
                sum += 10;
                i++;
            } else if (c == 'L') {
                sum += 50;
                i++;
            } else if (c == 'C') {
                sum += 100;
                i++;
            } else if (c == 'D') {
                sum += 500;
                i++;
            } else if (c == 'M') {
                sum += 1000;
                i++;
            } else if (c == 'I') {
                sum += 1;
                i++;
            } else if (c == 'V') {
                sum += 5;
                i++;
            } else if (c == 'X') {
                sum += 10;
                i++;
            } else if (c == 'L') {
                sum += 50;
                i++;
            } else if (c == 'C') {
                sum += 100;
                i++;
            } else if (c == 'D') {
                sum += 500;
                i++;
            } else if (c == 'M') {
                sum += 1000;
                i++;
            } else if (c == 'I') {
                sum += 1;*/
    }
}
    }
    
}
