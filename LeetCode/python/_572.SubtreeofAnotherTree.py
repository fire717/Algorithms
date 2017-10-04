# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from hashlib import sha256  #py计算hash值
class Solution(object):
    def isMatch(self, s, t):
        if not(s and t):
            return s is t #这个判断不错！
        return (s.val == t.val and 
            self.isMatch(s.left, t.left) and 
            self.isMatch(s.right, t.right))

    def isSubtree(self, s, t):
        if self.isMatch(s, t): return True  
        if not s: return False   #先判断两种特殊情况，相同和s为空
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t) #递归判断两个自述，直到两个可以match为止
        #返回的是布尔值
