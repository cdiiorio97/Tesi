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
        #BFS
        #Time: O(n)
        #Space: O(n)
        if not root: return None
        queue = [root]
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                if i == size - 1: return node.val
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        return None
        