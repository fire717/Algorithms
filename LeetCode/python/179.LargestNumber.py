#169ms-6%...不过好歹是自己做出来的
#是有点慢，应该是n*(n-1)的复杂度，不过代码思路简单呀

class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        if sum(nums)==0: #先判断全0的特殊情况
            return '0'
        l = len(nums)
        tmp = [str(i) for i in nums]
        for i in xrange(l-1):
            for j in xrange(i+1,l):
                if int(tmp[i]+tmp[j]) < int(tmp[j]+tmp[i]):#相等时才需要继续判断
                        tmp[i],tmp[j] = tmp[j],tmp[i]
        ans = ''
        for n in tmp:
            ans+=n
        return ans
