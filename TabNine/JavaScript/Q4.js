/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    //Given a roman numeral, convert it to an integer.
    //Input is guaranteed to be within the range from 1 to 3999.

    let result = 0;
    for (let i = 0; i < s.length; i++) {
        if (s[i] === 'I') {
            result += 1;
        } else if (s[i] === 'V') {
            result += 5;
        } else if (s[i] === 'X') {
            result += 10;
        } else if (s[i] === 'L') {
            result += 50;
        } else if (s[i] === 'C') {
            result += 100;
        } else if (s[i] === 'D') {
            result += 500;
        } else if (s[i] === 'M') {
            result += 1000;
        }
    }
    return result;        
}