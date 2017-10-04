#我的思路是先算有多少操作符n，然后得到(n-1)n种组合，然后分别计算。卡在不知道怎么分配顺序了
#查了下用递归，循环到每个操作符，递归其左右两边
class Solution:
    # @param {string} input
    # @return {integer[]}
    def diffWaysToCompute(self, input):
        ans = []
        for i in range(len(input)):
            c = input[i]
            if c in '+-*':
                a = self.diffWaysToCompute(input[:i])
                b = self.diffWaysToCompute(input[i + 1:])
                for m in a:
                    for n in b:
                        if c == '+':
                            ans.append(m + n)
                        elif c == '-':
                            ans.append(m - n)
                        elif c == '*':
                            ans.append(m * n)
        
        if not ans:
            ans.append(int(input))
        
        return ans
