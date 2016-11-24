# 看到一个分析不错
# 之前尝试一边计算深度，一边做判断，发现这是无法实现的。
# 因为bool型的返回变量说明了返回值没有深度信息，而如果没有深度信息，那么就无法判断左子树和右子树的深度差是否为1.
# 所以说明还要另外使用一个计算深度的函数来做辅助了。

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def Height(self, root):
        if root == None:
            return 0
        return max( self.Height( root.left ), self.Height( root.right ) ) + 1
    
    def isBalanced(self, root):
        if root  == None:
            return True
        if abs( self.Height( root.left ) - self.Height( root.right ) ) <= 1:
            return self.isBalanced( root.left ) and self.isBalanced( root.right )
        else:
            return False
        
