#迭代
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        perms = [[]]   
        for n in nums:
            new_perms = []
            for perm in perms:
                for i in xrange(len(perm)+1):   #每次扩大一位
                    new_perms.append(perm[:i] + [n] + perm[i:])   #每次在不同位置插入一个当前遍历的n
            perms = new_perms
            #print perms
'''
[[1]]
[[2, 1], [1, 2]]
[[3, 2, 1], [2, 3, 1], [2, 1, 3], [3, 1, 2], [1, 3, 2], [1, 2, 3]]
'''
        return perms

