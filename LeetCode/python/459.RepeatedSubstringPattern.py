#心态要稳，差点放弃去查，还是想出来了
#虽然慢了点662ms-14，后续应该可以优化，比如根据s总长度，可以在循环时只判断length为奇数或者偶数的
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = len(s)
        for length in xrange(1,l/2+1): #外循环为单个子str长度
            t = s[:]
            lenT = len(t)
            while lenT >0:
                if t[0:length]!=t[length:length*2]:
                    break
                t=t[length:]
                lenT = len(t)
                if lenT==length:
                    return True
        return False
