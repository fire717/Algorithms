# 写了个双重循环，果然超时了..有思路倒着比较，但是要先遍历完然后保存逆序？
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        ca = headA
        while ca !=None:
            cb = headB 
            while cb != None:
                if ca == cb:
                    return ca
                cb = cb.next
            ca = ca.next
        return                       #好吧，return null 要写成这样，null不是保留字
        
# 思路一关键点在于两链表的长度m、n(m>=n),长链表比短链表多走m-n步，这样两链表长度对应后，逐一比较就可以 
# 我去，这不就是考研里的一道题吗....唉 
# 醉了，网上搜了几个提交，都显示Memory Limit Exceeded ...好像要求是O(1)的空间复杂度
# 思路二不错： 链表到尾部后,跳到另一个链表的头部, 相遇点即为intersection points.看怎么判断相遇吧
# 但是找了好久么有python版本的，自己改写了一个c写的，提交还是MLE了...从论坛里搞了个ac的版本，依旧不行...不知道为啥,先放这吧...
class Solution(object):
    def getIntersectionNode(self, headA, headB): 
        cur1 = headA
        cur2 = headB
        while cur1!=cur2:
            if cur1!=None:
                cur1=cur1.next
            else:
                cur1 = headB
            if cur2!=None:
                cur2 = cur2.next
            else:
                cur2 = headA
        return cur1

#在论坛找个个AC的
class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None

        pa = headA # 2 pointers
        pb = headB

        while pa is not pb:
            # if either pointer hits the end, switch head and continue the second traversal, 
            # if not hit the end, just move on to next
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next

        return pa # only 2 ways to get out of the loop, they meet or the both hit the end=None

# the idea is if you switch head, the possible difference between length would be countered. 
# On the second traversal, they either hit or miss. 
# if they meet, pa or pb would be the node we are looking for, 
# if they didn't meet, they will hit the end at the same iteration, pa == pb == None, return either one of them is the same,None

