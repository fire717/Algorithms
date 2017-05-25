#45ms-47%
#10进制转2：int('xxx',2)
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        t = bin(num)[3:]
        ans=''
        for i in t:
            ans+=str(1-int(i))
        if not ans:#排除为空
            return 0
        return int(ans,2)
