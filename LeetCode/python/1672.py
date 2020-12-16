#执行用时：44 ms, 在所有 Python3 提交中击败了31.93%的用户
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        money_max = 0
        for i in range(len(accounts)):
            this_money = sum(accounts[i])
            if this_money>money_max:
                money_max = this_money
        return money_max
