# 104. Maximum Depth of Binary Tree  QuestionEditorial Solution  My Submissions
# Total Accepted: 180540
# Total Submissions: 362697
# Difficulty: Easy
# Given a binary tree, find its maximum depth.

# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Subscribe to see which companies asked this question


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        return root != None and 1 + max(self.maxDepth(root.left),self.maxDepth(root.right)) or 0

        
        if root == None:
            return 0
        left = None == root.left and 0 or self.maxDepth(root.left)
        right = None == root.right and 0 or self.maxDepth(root.right)
        
        return 1 + (left > right and left or right)