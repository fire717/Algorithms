# 好久没有独立做出来了...囧。153ms-31%
#用了一些python自带的方法，比如replace去掉'-'，upper大小写转换，len求长度，可能全部自己写然后只遍历一遍比较快吧
class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        originL=len(S)
        SS=S.replace('-','')
        l=len(SS)
        SS=SS.upper()
        firstS=l%K
        ans=SS[0:firstS]
        for i in range(firstS,l,K):
            if i!=0:
                ans+='-'
            for t in range(0,K):
                ans+=SS[i+t]
        return ans
