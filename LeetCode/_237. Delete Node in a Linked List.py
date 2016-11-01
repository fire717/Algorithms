# 想多了

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node): 
        """
        :type node: ListNode   要删除的结点
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node.next!=None:
            node.val = node.next.val
            node.next = node.next.next
