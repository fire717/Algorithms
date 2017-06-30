#最开始题目没理解好，只要非空字符串都算..
#39ms-55%

class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        space=' '
        l=len(s)
        i=0
        while i < l:
            if s[i] != space:
                j=1
                while (i+j)<l:
                    if s[i+j] == space:
                        count+=1
                        i=i+j+1
                        break
                    else:
                        j+=1
                if i+j==l and s[-1]!=space:
                    count+=1
                    break
            else:
                i+=1
        return count
