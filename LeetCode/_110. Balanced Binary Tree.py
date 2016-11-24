# 看到一个分析不错
# 之前尝试一边计算深度，一边做判断，发现这是无法实现的。
# 因为bool型的返回变量说明了返回值没有深度信息，而如果没有深度信息，那么就无法判断左子树和右子树的深度差是否为1.
# 所以说明还要另外使用一个计算深度的函数来做辅助了。

'''
解题思路：在这道题里，平衡二叉树的定义是二叉树的任意节点的两颗子树之间的高度差小于等于1。
这实际上是AVL树的定义。首先要写一个计算二叉树高度的函数，二叉树的高度定义为：树为空时，高度为0。
然后递归求解：树的高度 = max(左子树高度，右子树高度)+1(根节点要算上)。
高度计算函数实现后，递归求解每个节点的左右子树的高度差，如果有大于1的，则return False。如果高度差小于等于1，则继续递归求解。
'''

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
        
