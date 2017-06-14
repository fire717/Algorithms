# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        def _sum(node):
            if not node: return 0  #递归边界起点
            left, right = _sum(node.left), _sum(node.right)  #递归
            self.ans += abs(left - right)
            return node.val + left + right
        _sum(root)
        return self.ans
