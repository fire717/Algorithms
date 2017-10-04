class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        sort = sorted(nums)[::-1] #降序排序
        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"] + map(str, range(4, len(nums) + 1))
        #map(func,list)对list中每个元素进行一次func函数,这里就是生成一堆数字的字符串
        return map(dict(zip(sort, rank)).get, nums)
        #zip(),类似于把几个list按位置对应关系从新生成几组元组的list，比如这里就是sort排序与rank对应[（max(sort）,"Gold .."),..]
        #然后dict()转为字典
        #继续map函数，对nums分别应用dict.get()，由key(具体数字)得到value（排名str），注意上面没有()。
        
        #总结简单来说，就是先生成数字和排名对应的字典，然后利用dict.get()重新扫描一遍得到对应位置
