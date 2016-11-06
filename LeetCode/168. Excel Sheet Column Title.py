# 写出来这么简单几行，但是想了好久....
#关键问题在于处理26整除如何表示，参考十进制，模应该是27,但这里是没有0位的，相当于从9直接到11
# 或者，把A看成0？那模还是26就是这样，这里太绕了...写下来对应或许好点，不过还是直接写出来了...
# 1-A-0 2-B-1 3-C-2....
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        al = {}
        st = ord('A')                    #继续熟悉ord()与chr()，ascii与字符互换
        for i in range(1,27):           # 自动建立1-A开始对应的字典
            al[i]=chr(st+i-1)
        ans = ''
        while n>0:
            ans=al[(n-1)%26+1]+ans   #n-1是因为n是对应1开头的，所以把A看做0后要减一，然后转换时要+1来找对应关系
            n=(n-1)/26     #n-1是关键
        return ans
