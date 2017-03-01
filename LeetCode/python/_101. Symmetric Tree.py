# 对树还是弱鸡啊...等这段时间忙完有空老子要花一天的时间来研究！
# 好了，今日打卡完成，滚去复习考试了...
'''
1.停止条件是 left==None & right==None
2. left.val==right.val 比较left.left right.right & left.right right.left
任何条件不成立都是false
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:  
    # @param root, a tree node  
    # @return a boolean  
    def sym(self,left,right):  
        if left==None and right==None:  
            return True  
        if left and right and left.val==right.val:  
            return self.sym(left.left,right.right) and self.sym(left.right,right.left)  
        else:  
            return False  
              
    def isSymmetric(self, root):  
        if root==None:  
            return True  
        return self.sym(root.left,root.right)

