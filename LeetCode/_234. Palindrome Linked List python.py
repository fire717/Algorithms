#  O(n) time and O(1) space
#结合上道题思路，先让快指针走一半...也不行啊
#等等，快指针直接走到一半+1,慢指针边走边记录，然后到一半逆序走，试试！
#也不知道怎么判断为一半啊...
#c搜了一个。。不就是记录然后逆序比较嘛...好吧，O（1）SPACE这样也算O(n)=O（2n）
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head==None or head.next==None:return True
        resList=[]
        while head!=None:
            resList.append(head.val)
            head=head.next
    
        return resList==resList[::-1]
