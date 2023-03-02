/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var findBottomLeftValue = function(root) {

    //Given the root of a binary tree, return the leftmost value in the last row of the tree.
    if(root === null) return null;
    let left = findBottomLeftValue(root.left);
    let right = findBottomLeftValue(root.right);
    return root.val + Math.max(left, right);
}