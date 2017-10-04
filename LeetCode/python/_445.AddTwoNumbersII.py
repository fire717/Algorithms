#不知道怎么把list转为链表（类似的问题即动态给变量命名，不知道如何实现，也不知道这里需不需要）
#菜鸡如我的思路就是先转为list，处理完再转回去，下面的代码验证结果对，就差转回链表了..
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1l=[]
        l2l=[]
        ans=[]
        while l1.next != None:
            l1l.append(l1.val)
            l1=l1.next
        while l2.next != None:
            l2l.append(l2.val)
            l2=l2.next
        l1l.append(l1.val)
        l2l.append(l2.val)
        intp=0
        if l1l[0]+l2l[0]>=10:
            intp=1
        t=0
        len1=len(l1l)
        len2=len(l2l)
        if len1>len2:
            longl=l1l
            shortl=l2l
        else:
            shortl=l1l
            longl=l2l
        k=1
        while k<= len(shortl):
            if longl[-k] + shortl[-k] +t >=10:
                longl[-k]=longl[-k]+shortl[-k]+t-10
                t=1
            else:
                longl[-k]=longl[-k]+shortl[-k]+t
                t=0
            k+=1
        if len1!=len2:
            longl[-k]+=t
            ans=longl
        else:
            if intp:
                ans=[1]
                for x in longl:
                    ans.append(x)
            else:
                ans=longl
        return ans
        
#自己的解法已经能满足大多数情况了，但还是有个别情况不能AC，还是学习下标准解法算了        
#标准解法
class Solution(object):
    def reverse(self, l):
        if l is None or l.next is None:
            return l
        p1, p2, l.next = l, l.next, None
        while(p2 is not None):
            tmp, p2.next = p2.next, p1
            p1, p2 = p2, tmp
        return p1
            
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        # align two lists using two pointers
        p1, p2, flag = l2, l1, 0
        while (flag<2):
            if p1.next is None:
                p1 = l1
                flag += 1
            else:
                p1 = p1.next
            if p2.next is None:
                p2 = l2
                flag += 1
            else:
                p2 = p2.next

        
        # initialize: deep copy the longer list
        pp = l1 if p1!=l1 else l2
        pp3, p3, l3 = None, None, None
        while (pp is not None):
            if l3 is None:
                l3 = ListNode(pp.val)
                pp3 = l3
            else:
                pp3.next = ListNode(pp.val)
                pp3 = pp3.next
            if pp==p1 or pp==p2:
                p3 = pp3
            pp = pp.next

        # add
        pp1, pp2, pp3 = p1, p2, p3
        while (pp1 is not None):
            pp3.val = pp1.val + pp2.val
            pp1, pp2, pp3 = pp1.next, pp2.next, pp3.next
            
        pp = l3

        # reverse, adjust, reverse
        rl3 = self.reverse(l3)
        pp = rl3
        carry, p = 0, rl3
        while (p.next is not None):
            carry, p.val = divmod(p.val+carry, 10)
            p = p.next
        carry, p.val = divmod(p.val+carry, 10)
        p.next = ListNode(carry) if carry != 0 else None
        l3 = self.reverse(rl3)
        return l3
