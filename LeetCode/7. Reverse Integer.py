# 思路一开始就想好了，只是忽略了溢出的问题，记录下32位范围是2**31

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        limit = 2**31
        n = 0
        t = 0                #用来保存x正负性，然后统一转为正数处理
        if x>limit-1 or x<-limit:          #还要判断溢出...
            return 0
        if x<0:
            t=1
            x = -x
        while x>0:
            n=n*10+x%10
            x/=10
        if n<limit:
            if t == 0 :
                return n
            else:
                return -n
        else:
            return 0
