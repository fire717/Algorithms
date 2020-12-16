"""
执行用时：
248 ms
, 在所有 Python3 提交中击败了
100.00%
的用户
内存消耗：
14.7 MB
, 在所有 Python3 提交中击败了
100.00%
的用户
"""

class Solution:
    def minPartitions(self, n: str) -> int:
        max_num = 0
        for i in range(len(n)):
            value = int(n[i])
            if value > max_num:
                max_num = value

        return max_num
