package Java;

public class Q5 {
    public boolean searchMatrix(int[][] matrix, int target) {
        /*You are given an m x n integer matrix matrix with the following two properties:
        *Each row is sorted in non-decreasing order.
        *The first integer of each row is greater than the last integer of the previous row.
        *Given an integer target, return true if target is in matrix or false otherwise.
        *You must write a solution in O(log(m * n)) time complexity. 
        */
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return false;
        }
        int m = matrix.length;
        int n = matrix[0].length;
        int start = 0;
        int end = m * n - 1;
        while (start + 1 < end) {
            int mid = start + (end - start) / 2;
            if (matrix[mid / n][mid % n] == target) {
                return true;
            } else if (matrix[mid / n][mid % n] < target) {
                start = mid;
            } else {
                end = mid;
            }
        }
        if (matrix[start / n][start % n] == target) {
            return true;
        } else if (matrix[end / n][end % n] == target) {
            return true;
        } else {
            return false;
        }
    }
}
