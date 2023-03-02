/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    //Given a string s, find the length of the longest substring without repeating characters.
    

    let max = 0;

    for (let i = 0; i < s.length; i++) {

                for (let j = i + 1; j < s.length; j++) {

                    if (s[i] === s[j]) {
                        max = Math.max(max, j - i);
                    }
                }
            }

    return max;
};


