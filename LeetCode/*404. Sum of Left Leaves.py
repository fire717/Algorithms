# 注意看题，self.val = x

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root :
            if root.left != None and root.left.left == None and root.left.right == None :
                return root.left.val + self.sumOfLeftLeaves(root.right)
            else:
                return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
        else:return 0
