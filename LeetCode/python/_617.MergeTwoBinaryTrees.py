# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1 and not t2:
            return None
        
        elif t1 and not t2:
            return t1
        
        elif t2 and not t1:
            return t2
        
        r = TreeNode(t1.val + t2.val)
        r.left = self.mergeTrees(t1.left, t2.left)
        r.right = self.mergeTrees(t1.right, t2.right)
        return r
