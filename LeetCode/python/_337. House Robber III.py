#又是动态规划.
#函数内还能定义函数，学到了

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root) :  
            if not root : return [0, 0]  
            robLeft = dfs(root.left)  
            robRight = dfs(root.right)  
            norobCur = robLeft[1] + robRight[1]  
            robCur = max(robLeft[0] + robRight[0] + root.val, norobCur)  
            return [norobCur, robCur]  
        return dfs(root)[1]  
