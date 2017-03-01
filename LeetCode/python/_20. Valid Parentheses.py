# 熟悉栈的思想但是使用还是不熟悉，这里是用dict构造对，学习下。同时熟悉了pop()方法

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pars = [None]
        parmap = {')': '(', '}': '{', ']': '['}
        for c in s:
            if c in parmap and parmap[c] == pars[-1]:
                pars.pop()
            else:
                pars.append(c)
        return len(pars) == 1
