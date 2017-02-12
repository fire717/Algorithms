#汉明距离是将一个字符串变换成另外一个字符串所需要替换的字符个数。
#思路是考虑所有数字的同一个bit位，统计在这个bit位上出现的1的次数count，那么这个bit位在总的汉明距离中就贡献了count*(n-count)，n是数组中元素的个数。

class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        res = 0
        lists = []
        nums.sort()
        for i in nums:
            temp = list(bin(i)[2:])
            temp.reverse()
            lists.append(temp)

        for i in range(len(lists[-1])):
            count_0, count_1 = 0, 0
            for element in lists:
                # print element
                if len(element)-1 < i:
                    count_0 += 1
                elif element[i] == '0':
                    count_0 += 1
                elif element[i] == '1':
                    count_1 += 1
                # print count_0,count_1
            res += count_0 * count_1
        return res

