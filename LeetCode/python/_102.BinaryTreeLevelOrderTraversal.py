# 宽度优先，好像练过m，忘了...
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if root == None:
            return res

        q = [root]
        while len(q) != 0:
            res.append([node.val for node in q])        #注意这里的[]，z为了题目格式
            new_q = []                                #用一个新列表保存遍历的本行的节点，然后赋值给原循环列表
            for node in q:
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)
            q = new_q

        return res
