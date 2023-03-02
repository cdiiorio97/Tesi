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
   
    if (matrix.length === 0 || matrix[0].length === 0) {
        return false;
    }
    let m = matrix.length;
    let n = matrix[0].length;
    let i = 0;
    let j = n - 1;
    while (i < m && j >= 0) {
        if (matrix[i][j] === target) {
            return true;
        } else if (matrix[i][j] < target) {
            i++;
        } else {
            j--;
        }
    }
    return false;
};