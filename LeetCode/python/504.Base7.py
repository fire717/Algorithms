#39ms-91%
#很简单的题居然卡了一会，主要就是借鉴模仿转2进制的思想
#相当于转为7进制
class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num==0:
            return '0'
        tag = 0
        if num <0:
            num = -num
            tag = 1
            
        res = ''
        while num: #从低位到高位每位为当前7的余数
            res = str(num%7)+res
            num/=7
            
        if tag:
            res='-'+res
        return res
