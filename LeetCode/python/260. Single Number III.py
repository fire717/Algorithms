# 1199 ms-3.9%.....不过也算是自己独立做出来的 先放着 后面再优化吧
# list.remove(obj)  移除列表中某个值的第一个匹配项

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        t = []
        for x in nums:
            if x not in t:
                t.append(x)
            else:
                t.remove(x)
        return t
