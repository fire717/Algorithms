#将四数转变为两个部分
#首先遍历AB的组合（任意两个都可以），存下他们组合后的和的情况，然后遍历CD（另外两个）的和，
#看之前AB遍历的组合里有没有与此时值相反的值，有的话就加上AB中这个相反数出现的次数。

class Solution(object):  
    def fourSumCount(self, A, B, C, D):  
        res2 = {}  
        res = 0  
  
        for i in C:  
            for j in D:  
                res2[i+j] = res2.get(i+j,0) + 1  
  
        for i in A:  
            for j in B:  
                res += res2.get(-i-j,0)  
  
        return res  
