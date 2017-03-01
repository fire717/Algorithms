# 没思路，难道要遍历求和保存吗
# 好吧，因为是根到叶，所以真的遍历.
# 没找到PYTHON解法，参考了一个c的,还调了好久...。对树的遍历还是不熟悉

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:return False
        if root.left==None and root.right==None and root.val==sum:   #root if a leaf
            return True
        if self.hasPathSum(root.left,sum-root.val):               #sum-root.val!!!
            return True
        if self.hasPathSum(root.right,sum-root.val): 
            return True
        return False


