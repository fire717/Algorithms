#只能一次遍历，没有思路
#用两个指针 fast 和slow。 fast先走n 步,slow这时候从头开始走，当fast走到尾的时候slow就走到需要跳过的位置了。
#这样只需要走一遍就可以了。跟那道题思路一样...

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy=ListNode(0)
        dummy.next=head
        fast=dummy
        slow=dummy
        while n>0:
            fast=fast.next
            n-=1
        while fast.next:
            fast=fast.next
            slow=slow.next
        slow.next=slow.next.next
        return dummy.next
        
