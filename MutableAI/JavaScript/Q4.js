/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    //Given a roman numeral, convert it to an integer.
    //Input is guaranteed to be within the range from 1 to 3999.
    //Example:
    //Input: "XIV"
    //Output: 14
    //Input: "XIX"
    //Output: 19
    //Input: "XCIX"
    //Output: 99
    //Input: "XCIV"
    //Output: 94
    //Input: "XCIX"
    //Output: 99
    //Input: "XCIV"
    //Output: 94
    //Input: "XCIX"
    //Output: 99
    //Input: "XCIV"
    //Output: 94
    //Input: "XCIX"
    //Output: 99

    //1. Create a hashmap with the roman numeral as the key and the integer
    //2. Loop through the string and add the values to the integer
    //3. Return the integer
    let hashMap = {
        I: 1,
        V: 5,
        X: 10,
        L: 50,
        C: 100,
        D: 500,
        M:
        1000,
    };
    let integer = 0;
    for (let i = 0; i < s.length; i++) {
        if (i + 1 < s.length && hashMap[s[i]] < hashMap[s[i + 1]]) {
            integer -= hashMap[s[i]];
        } else {
            integer += hashMap[s[i]];
        }
    }
    return;
}