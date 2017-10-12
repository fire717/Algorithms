# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        info = []
        def dfs(node, depth = 0):
            if node:
                if len(info) <= depth: #同一层添加过后则不添加了
                    info.append([0, 0])
                info[depth][0] += node.val
                info[depth][1] += 1
                dfs(node.left, depth + 1)  #从这里递归
                dfs(node.right, depth + 1)
        dfs(root)

        return [s/float(c) for s, c in info]
