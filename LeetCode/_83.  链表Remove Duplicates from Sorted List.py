# 对链表操作还是不熟悉啊，不知道怎么遍历。一行行分析代码，终于勉强理解了...
# 对链表节点操作，head赋值给x后，操作x，head一样会变，因为head本质是指针，是地址

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:  
            return head  
        pre = head  
        cur = head.next  
        while cur != None:                         #当cur节点非空
            if cur.val != pre.val:               #如果cur的值不等于pre的值，pre和cur指针后移一位
                pre = cur  
                cur = cur.next  
                continue                    #这里可以结束本次循环，那么后面就是cur和pre值相等的情况了           
            while cur.next != None and cur.next.val == pre.val:          #节约时间，一次性把所有和pre值相同的去掉
                cur = cur.next  
            pre.next = cur.next               #这里就消去了cur节点，关键！
            cur = pre.next                  #继续后面的循环，所以重新生成cur
        return head 
