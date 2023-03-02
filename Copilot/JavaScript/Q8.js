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

    //BFS
    let queue = [root];
    let result = root.val;
    while(queue.length){
        let size = queue.length;
        for(let i = 0; i < size; i++){
            let node = queue.shift();
            if(i === 0) result = node.val;
            if(node.left) queue.push(node.left);
            if(node.right) queue.push(node.right);
        }
    }
    return result;
    
};