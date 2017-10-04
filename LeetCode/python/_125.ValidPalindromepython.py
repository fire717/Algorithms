# 查到了是回文的意思，但是一开始居然没看懂题目...原来忽略掉符号只看子母就行...
# 查了一个，写的好简洁啊


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cleanlist = [c for c in s.lower() if c.isalnum()]        # 判断是否只含数字和字母，而题目又说只有字母
        return cleanlist == cleanlist[::-1]
        
# 稍微改了下，判断一半就行。68ms-96% > 88ms-74%
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cleanlist = [c for c in s.lower() if c.isalnum()]
        l = len(cleanlist)
        backlist = cleanlist[::-1]                                   #试了下不能s[a:b;-1],只能分开来了
        return cleanlist[0:l/2] == backlist[0:l/2]
