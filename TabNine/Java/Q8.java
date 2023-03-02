package Java;

import javax.swing.tree.TreeNode;

public class Q8 {
    public int findBottomLeftValue(TreeNode root) {
        //Given the root of a binary tree, return the leftmost value in the last row of the tree.
        if(root == null)
            return -1;
        int left = findBottomLeftValue(root.left);
        int right = findBottomLeftValue(root.right);
        if(left == -1 || right == -1)
            return -1;
        return Math.max(left, right);
    }
}
