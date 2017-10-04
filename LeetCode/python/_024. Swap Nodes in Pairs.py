# 思路要清晰

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = ListNode(0)
        pre.next = head
        curr = head
        head = pre
        while curr and curr.next:      # curr =1, curr.next =2
            pre.next = curr.next       # 0 --> 2
            curr.next = pre.next.next  # 1 --> 3  # curr.next.next
            pre.next.next = curr       # 3 --> 1
            pre = curr                 # pre = 1
            curr = curr.next           # curr= 3
        return head.next
