# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #Given the root of a binary tree, return the leftmost value in the last row of the tree.
        

        if not root:
            return -1
        
        stack = [root]

        while stack:

            node = stack.pop()
            
            if node.left:
                stack.append(node.left)
            
            if node.right:
                stack.append(node.right)

        return
    
    