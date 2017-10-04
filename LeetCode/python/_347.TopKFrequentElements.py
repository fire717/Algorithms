#时间复杂度只有O(n)的桶排序（bucket sort），同时消耗空间复杂度O(n)
# 学习了用二重list表示二重信息的思路
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        data, res = {}, []
        for i in nums:
            data[i] = data[i] + 1 if i in data else 1      #这个写的简洁，学习/统计每个数字出现次数
        bucket = [[] for i in xrange(len(nums)+1)]     #生成多维空列表
        for key in data:                          #字典遍历
            bucket[data[key]].append(key)       #子列表索引号为出现次数，列表里的值为该出现次数的数字（可能有相同次数的）
        for i in xrange(len(bucket)-1, -1, -1):  #逆序输出即为从大到小了
            if bucket[i]:
                res.extend(bucket[i])   # extend()方法只接受一个列表作为参数，并将该参数的每个元素都添加到原有的列表中。
            if len(res) >= k:
                break
        return res[:k]
