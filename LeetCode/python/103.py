"""
执行用时：
48 ms
, 在所有 Python3 提交中击败了
22.06%
的用户
内存消耗：
15.1 MB
, 在所有 Python3 提交中击败了
5.03%
的用户
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root) -> List[List[int]]:
        if not root:
            return []
        res = []
        layer_now = [root]
        layer_next = []

        flag = 0
        while layer_now:
            layer_value = []
            for node in layer_now:
                layer_value.append(node.val)
                if node.left:
                    layer_next.append(node.left)
                if node.right:
                    layer_next.append(node.right)

            if flag:
                layer_value = layer_value[::-1]
            flag = 1-flag
            res.append(layer_value)
            layer_now = layer_next.copy()
            layer_next = []
        return res
