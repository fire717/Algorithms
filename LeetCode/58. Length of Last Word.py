# 调了比较久...熟悉了.strip()方法m，

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.strip()   #str.strip()去掉字符串开头和结尾的空格
        if len(s)<=1:
            if len(s)<1:
                return 0
            else:
                return 1 if s[0]!=' ' else 0
        s=' '+s            #统一加一个空格以方便判断
        count = 1
        i=-1
        while s[i-1]!=' ':
            count+=1
            i-=1
        return count
