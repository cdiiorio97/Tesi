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

        } else {
            int leftDepth = maxDepth(root.left); 
            int rightDepth = maxDepth(root.right);
            /*
            * nelle due righe precedenti, segna un errore per left e right (cannot be resolved or is not a field)
            * però sulla pagina di LeetCode, il codice funziona comunque
            */

            if (leftDepth > rightDepth) {
                return leftDepth + 1;
            } else {
                return rightDepth + 1;
            }
        }        
    }
}
