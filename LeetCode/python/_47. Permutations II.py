class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums: #先判断非空
            return []
        nums.sort()
        ret = [[]]
        for n in nums:
            new_ret = []
            l = len(ret[-1])
            for seq in ret:
                for i in range(l, -1, -1):#从l逆序到-1，不包括-1
                    if i < l and seq[i] == n:
                        break
                    new_ret.append(seq[:i] + [n] + seq[i:]) #把第i个位置设为n
            ret = new_ret
        return ret
