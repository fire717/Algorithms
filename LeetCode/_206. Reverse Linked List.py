# 思路一利用栈结构，将链表内容依次压入栈，再从栈依次弹出即可构造逆序。下面的代码用普通数组模拟栈。

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head  
        newList = []
        while p:
            newList.insert(0, p.val)       #了解了insert的用法及栈的构造
            p = p.next                      #因为这里不断把p.next覆盖p，所以之前要把head赋给p
        p = head                            
        for v in newList:
            p.val = v
            p = p.next
        return head                     #上面是改变p，为什么可以return head?
        
# 思路二与思路一栈的思想类似，不过是直接在原链表操作，通过迭代将节点重组，前面的节点转移到重组链表的后面。实际上就是头结点倒插操作。
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_head = None
        while head:
            p = head
            head = head.next
            p.next = new_head         # 把第一个节点后的就覆盖了
            new_head = p
        return new_head
