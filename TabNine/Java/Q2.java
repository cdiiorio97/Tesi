package Java;

import javax.swing.tree.TreeNode;

public class Q2 {
    public int maxDepth(TreeNode root) {
        /*
         * Given the root of a binary tree, return its maximum depth.
         * A binary tree's maximum depth is the number of nodes along the longest path 
         * from the root node down to the farthest leaf node.
         */

         if (root == null) {
             return 0;
         }
         int left = maxDepth(root.left);
         int right = maxDepth(root.right);
         return Math.max(left, right) + 1;
        }
         
}
