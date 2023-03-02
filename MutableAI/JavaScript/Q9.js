/**
 * @param {string} s
 * @return {string}
 */

    //You are given a string s. You can convert s to a palindrome by adding characters in front of it.

    var shortestPalindrome = function(s) {
        var len = s.length;
        if (len <= 1) return s;
        var i = 0;
        var j = len - 1;
        while (i < j) {
            if (s[i] === s) {
                i++;
            } else if (s[j] === s) {
                j--;
            } else {
                break;
            }
        }
        if (i >= j) return s;
        var left = s.substring(0, i);
        var right = s.substring(j + 1);
        var mid = s.substring(i, j + 1);
        var midReverse = mid.split("").reverse().join("");
        var result = left + midReverse + right;
        return result;
    }