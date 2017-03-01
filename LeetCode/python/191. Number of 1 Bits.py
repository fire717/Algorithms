#

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0 
        s = ''
        while n>0:
            s+='%d' %(n%2)    #一开始没过，原来是这里要加括号，不然取余号就混淆了
            n/=2
        return len(s.replace('0',''))
