"""
执行用时：
72 ms
, 在所有 Python3 提交中击败了
90.56%
的用户
内存消耗：
20.9 MB
, 在所有 Python3 提交中击败了
23.34%
的用户
"""
# 面试题 08.07. 无重复字符串的排列组合
# 貌似出自《程序员面试金典》？后面这一类多了再放到一个地方吧
# https://leetcode-cn.com/problems/permutation-i-lcci/
# 看了提示思路才做出来，思路是每次不同位置加一个元素形成新组合
class Solution:
    def permutation(self, S: str):
        def _addOne(history_s, s):
            s_list = [s+history_s, history_s+s]
            for i in range(1,len(history_s)):
                new_s = history_s[:i]+s+history_s[i:]
                s_list.append(new_s)
            return s_list

        res = [S[0]]
        for s in S[1:]:
            res_new = []
            for history_s in res:
                #print(history_s, s)
                history_s_add_one = _addOne(history_s, s)
                #print(history_s_add_one)
                res_new.extend(history_s_add_one)
            res = res_new
        return res
