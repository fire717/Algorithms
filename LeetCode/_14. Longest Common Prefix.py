# 又是题目没读懂...
# 给一个字符串数组，要找到这些字符串的最大前缀公共子串。

class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        for i, letter_group in enumerate(zip(*strs)):       #【enumerate】函数可以同时返回列表或元组等可迭代对象的下标和内容           
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        else:
            return min(strs)
       ''' 
       zip函数可以接受一系列的可迭代对象作为参数，将对象中对应的元素打包成一个个tuple(元组)，
       然后由这些tuple(元组)组成一个list(列表)，故其返回值为list(列表)，而如果传入的可迭代对象的长度不一致，
       则返回可迭代对象中最短的一个对象的长度，而其，通过zip(*list)可以将原打包的可迭代对向分开
       '''
