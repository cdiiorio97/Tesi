package Java;

import javax.swing.tree.TreeNode;

public class Q8 {
    public int findBottomLeftValue(TreeNode root) {
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
        if(root == null) return 0;           
        int[] res = new int[1];           
        helper(root, res, 0);           
        return res[0];           
    }           
    public void helper(TreeNode root, int[] res, int level) {           
        if(root == null) return;           
        if(level == res.length - 1) {           
            res[level] = root.val;           
            return;           
        }           
        helper(root.left, res, level + 1);           
        helper(root.right, res, level + 1);           
    }           
}