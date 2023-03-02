/**
 * @param {string} s
 * @return {string}
 */
var shortestPalindrome = function(s) {
    //You are given a string s. You can convert s to a palindrome by adding characters in front of it.

    //Return the shortest palindrome you can find.
    var n = s.length;
    if (n <= 1) return s;
    var dp = new Array(n);
    dp[0] = s[0];
    dp[n - 1] = s[n - 1];
    for (var i = 1; i < n; i++) {
        dp[i] = dp[i - 1] + s[i];
    }
    for (var i = n - 2; i >= 0; i--) {
        dp[i] = dp[i + 1] + s[i];
    }
    return dp[0];
        
    };