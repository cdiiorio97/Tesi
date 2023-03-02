/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function(matrix, target) {
    /*You are given an m x n integer matrix matrix with the following two properties:
    *Each row is sorted in non-decreasing order.
    *The first integer of each row is greater than the last integer of the previous row.
    *Given an integer target, return true if target is in matrix or false otherwise.
    *You must write a solution in O(log(m * n)) time complexity.
    */
   
    let m = matrix.length;
    let n = matrix[0].length;
    let left = 0;
    let right = m * n - 1;
    while (left <= right) {
        let mid = Math.floor((left + right) / 2);
        let midVal = matrix[Math.floor(mid / n)][mid % n];
        if (midVal === target) {
            return true;
        } else if (midVal > target) {
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    return false;
};