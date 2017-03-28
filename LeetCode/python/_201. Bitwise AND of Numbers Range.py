#超时了...也就遍历两次嘛
class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        tmp = []  
        l = len(bin(m))-2 #转二进制前两位固定为0b
        for i in xrange(m,n+1):
            newN = bin(i)[-l:]
            tmp.append(newN)
        zeroNum = []
        for i in tmp:
            for j in range(l):
                if i[j]=='0':
                    zeroNum.append(j)
        ans = ''
        for i in range(l):
            if i in zeroNum:
                ans+='0'
            else:
                ans+='1'
        return int(ans,2)
        
        
#AC版本
class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        i = 0
        while m != n:
            m >>= 1
            n >>= 1
            i += 1
        return n << i
