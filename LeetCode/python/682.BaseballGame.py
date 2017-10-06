#45 ms - 48%    一次提交AC
class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        valid_nums = [int(ops[0]) ]
        for i in ops[1:]:
            round_sc = 0
            if i == 'D':
                valid_nums.append(valid_nums[-1]*2)
            elif i == 'C':
                valid_nums.pop()
            elif i == '+':
                valid_nums.append(valid_nums[-1] + valid_nums[-2])
            else:
                valid_nums.append(int(i))
        return sum(valid_nums)
