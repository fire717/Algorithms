# 接触到二叉树才发现自己数据结构能考试但实际掌握的并不好，回顾了一下遍历，还是没有思路，无奈先百度了
# 提炼下解题思想：先令root return 0，然后一层层s向上递归，每一层加一

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return 0  
        leftDepth = self.maxDepth(root.left)  
        rightDepth = self.maxDepth(root.right)  
        return leftDepth + 1 if leftDepth > rightDepth else rightDepth + 1 
        #最后一行试了下换成下面这个也是可以的，用了max函数但是更简洁,但上面这张do sth if的j语法也要熟悉
        #return max(leftDepth + 1,rightDepth + 1) 
