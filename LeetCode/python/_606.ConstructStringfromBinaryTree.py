'''
We do this recursively.

If the tree is empty, we return an empty string.
We record each child as '(' + (string of child) + ')'
If there is a right child but no left child, we still need to record '()' instead of empty string.
'''
#'{}{}'.format() 格式化字符串
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t: return ''
        left = '({})'.format(self.tree2str(t.left)) if (t.left or t.right) else ''
        right = '({})'.format(self.tree2str(t.right)) if t.right else ''
        return '{}{}{}'.format(t.val, left, right)
