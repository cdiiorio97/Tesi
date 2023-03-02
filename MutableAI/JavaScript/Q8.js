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

    //Example 1:
    //Input: root = [1,3,2]
    //Output: 2
    //Explanation: The tree is like this:                1
    //     3                                               / \
    //     2                                              2   3
    //The leftmost value is 2, which is the value of the node with label 2.
    
    //Example 2:
    //Input: root = [1,2,3,4
    //Output: 4
    //Explanation: The tree is like this:                1
    //     2                                               / \
    //     3                                              3   4
    //     4                                              /

    //Example 3:
    //Input: root = [1,2,3,null,4,null,5,null,6,null,7,null,
    //Output: 7
    //Explanation: The tree is like this:                1
    //     2                                               / \
    //     3                                              null null
    //     null                                              4 5 6 7 null null null null null null null null null
    //Note:
    //The number of nodes in the tree will be between 1 and 100.
    //The values of the nodes in the tree will be between 1 and 100.
    //The width of the tree will be between 1 and 10.

    //Solution 1: BFS
    //Time Complexity: O(n) where n is the number of nodes in the tree
    //Space Complexity: O(n) where n is the number of nodes in the tree
    //var queue = [root]; var res = []; var level = 0; var maxLevel
    //while (queue.length) { var size = queue.length; var nextLevel =
    //while (size--) { var node = queue.shift(); if (node.left) queue.push(node.left); if (node.right) queue.push(node
    //if (size === 0) { if (level > maxLevel) { maxLevel =
    //res = node.val; } else if (level === maxLevel) { res = Math.min(res, node.val); } level++; } } } return res
    //Solution 2: DFS Recursion && DFS Iteration && DFS Iteration with
    //Time Complexity: O(n) where n is the number of nodes in the tree.
    //Space Complexity: O(n) where n is the number of nodes in the tree.
    //var res = Number.MAX_SAFE_INTEGER; var
    //function dfs(node, level) { if (!node) return; if (level
    //if (level > res) { res = level; } dfs(node.left
    //dfs(node.right, level + 1); } dfs(root, 1); return res; }
    //var res = Number.MAX_SAFE_INTEGER; var queue = [
        //{ node: root, level: 1 }]; while (queue.length) { var
        //{ node: node, level: level } = queue.shift(); if (node.
        //if (level > res) { res = level; } if (node.left) queue.push(node.left); if (node.right) queue.push(node
        //if (node.left) queue.push({ node: node.left, level:
        //if (node.right) queue.push({ node: node.right, level: level + 1 }); } return res; }
        //Solution 3: DFS Recursion && DFS Iteration && DFS Iteration with
        //Time Complexity: O(n) where n is the number of nodes in the tree.
        //Space Complexity: O(n) where n is the number of nodes
        //var res = Number.MAX_SAFE_INTEGER; var stack = [
        //{ node: root, level: 1 }]; while (stack.length) { var { node: node, level: level } = stack.shift(); if (node.left
        //if (level > res) { res = level; } if (node.right) stack.push({ node: node.right, level: level + 1 }); if (node
        //if (node.left) stack.push({ node: node.left, level: level + 1 }); } return res; }
       