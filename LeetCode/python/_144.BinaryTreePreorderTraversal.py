#Note: Recursive solution is trivial, could you do it iteratively?
#Classical usage of stack's LIFO feature, very easy to grasp:
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        stack = [root] #用栈保存节点
        while stack: 
            node = stack.pop() #弹出的是list最后的
            if node: #若存在
                ret.append(node.val) #保存跟节点值
                stack.append(node.right) #先加右子树，因为要先处理索引-1的
                stack.append(node.left)
        return ret
