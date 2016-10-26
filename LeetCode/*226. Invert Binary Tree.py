# 开始一直提示AttributeError: 'NoneType' object has no attribute 'left'，原来是要先判断节点存在。
# 虽然是自己写的，但是还是有点不理解后面两个if和最后return的关系，根据这个例子看来递归前面不一定要加return，只要递归函数内部有return即可。
# 同时，是先return再运算if里的递归的函数的,很奇怪，先标*吧


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            if root.left or root.right:
                x = root.left
                root.left = root.right
                root.right = x
                if root.left:
                    self.invertTree(root.left)
                if root.right:
                    self.invertTree(root.right)
            return root
