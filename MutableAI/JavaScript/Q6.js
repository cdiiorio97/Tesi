/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    //Given a string s, find the length of the longest substring without repeating characters.
   
    //Example 1:
    //Input: s = "abcabcbb"
    //Output: 3
    //Explanation: The answer is "abc", with the length of 3.
    //Example 2:
    //Input: s = "bb
    //Output: 1
    //Explanation: The answer is "b", with the length of 1.
    //Example 3:
    //Input: s = "p
    //Output: 1
    //Explanation: The answer is "p", with the length of 1.
    //Example 4:
    //Input: s = "p
    //Output: 2
    //Explanation: The answer is "p", with the length of 2.

    //Constraints:
    //The length of s will not exceed 15.
    //s consists of only lowercase English letters.
    //s is guaranteed to be a substring of a string of length n.
    
    //Solution 1: Brute Force
    //Time Complexity: O(n^2)
    //Space Complexity: O(1) since we are not using any extra space.
    //let max = 0
    //for (let i = 0; i < s.length; i++) {
        //for (let j = i + 1; j < s.length; j++) {
            //let temp = s.slice(i, j + 1)
            //let set = new Set(temp)
            //if (set.size === temp.length) {
                //max = Math.max(max, temp.length)
                //break
            //}
            //}		
        //}		
        //return max

    //Solution 2: Sliding Window (Two Pointers)
    //Time Complexity: O(n) since we are iterating through the string once.
    //Space Complexity: O(1) since we are not using any extra space.
    let max = 0;
    let start = 0;
    let end = 0;
    let map = new Map()
    while (end < s.length) {
        if (!map.has(s[end])) {
            map.set(s[end], end)
            end++
            max = Math.max(max, end - start)
        } else {
            start = map.get(s[end]) + 1
            map.set(s[end], end)
            end++
        }
    }
    return max;
}
