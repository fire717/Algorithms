#如何不改变值得遍历链表还是不熟悉。。。
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
    
        if head.next == None:
            return head
        
        pointer = head #设置一个指针
        length = 1
    
        while pointer.next:
            pointer = pointer.next
            length += 1  #遍历一遍得到长度
    
        rotateTimes = k%length  #考虑k太大的情况取余数
    
        if k == 0 or rotateTimes == 0:#整除时不用交换
            return head
    
        fastPointer = head #快慢两个指针 / 指先到第k个的
        slowPointer = head 
    
        for a in range (rotateTimes):
            fastPointer = fastPointer.next #指到待交换的最后一个
    
    
        while fastPointer.next:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next
    
        temp = slowPointer.next #暂存下头结点
    
        slowPointer.next = None
        fastPointer.next = head #此时fast指向尾节点
        head = temp
    
        return head
