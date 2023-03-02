package Java;

import javax.swing.tree.TreeNode;
    //Given the root of a binary tree, return the leftmost value in the last row of the tree.
    /**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public int findBottomLeftValue(TreeNode root) {
        int[] ans = new int[2];
        ans[0] = 0;
        ans[1] = root.val;
        findBottomLeftValue(root, 0, ans);
        return ans[1];
        
    }

    private void findBottomLeftValue(TreeNode root, int i, int[] ans) {
        if (root == null) {
            return;
        }
        if (i > ans[0]) {
            ans[0] = i;
            ans[1] = root.val;
        }
        findBottomLeftValue(root.left, i + 1, ans);
        findBottomLeftValue(root.right, i + 1, ans);

    }
}




