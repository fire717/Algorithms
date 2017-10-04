#一次性AC
#42ms-68%
class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        countA = 0
        countL = 0
        for i in s:
            if i == 'A':
                countL = 0
                if countA == 1 : #加之前就可以判断了
                    return False
                countA += 1
            elif i == 'L':
                if countL == 2:
                    return False
                countL += 1
            else:
                countL = 0
        return True
