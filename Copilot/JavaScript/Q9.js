/**
 * @param {string} s
 * @return {string}
 */

    //You are given a string s. You can convert s to a palindrome by adding characters in front of it.

var shortestPalindrome = function(s) {
    let rev = s.split('').reverse().join('');
    let l = s.length;
    for(let i = 0; i < l; i++){
        if(s.substring(0, l - i) === rev.substring(i)){
            return rev.substring(0, i) + s;
        }
    }
    return "";
};