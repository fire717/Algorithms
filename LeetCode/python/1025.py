"""
执行用时：
112 ms
, 在所有 Python3 提交中击败了
11.42%
的用户
内存消耗：
14.7 MB
, 在所有 Python3 提交中击败了
9.62%
的用户


在「方法一」中，我们写出了前面几项的答案，在这个过程中我们发现，Alice 处在 N = kN=k 的状态时，他（她）做一步操作，必然使得 Bob 处于 N = m (m < k)N=m(m<k) 的状态。因此我们只要看是否存在一个 mm 是必败的状态，那么 Alice 直接执行对应的操作让当前的数字变成 mm，Alice 就必胜了，如果没有任何一个是必败的状态的话，说明 Alice 无论怎么进行操作，最后都会让 Bob 处于必胜的状态，此时 Alice 是必败的。

结合以上我们定义 f[i]f[i] 表示当前数字 ii 的时候先手是处于必胜态还是必败态，\textit{true}true 表示先手必胜，\textit{false}false 表示先手必败，从前往后递推，根据我们上文的分析，枚举 ii 在 (0, i)(0,i) 中 ii 的因数 jj，看是否存在 f[i-j]f[i−j] 为必败态即可。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/divisor-game/solution/chu-shu-bo-yi-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""

class Solution:
    def divisorGame(self, N: int) -> bool:
        #1 <= N <= 1000

        if N==1:
            return False


        res_dict = [False]*(N+1)

        res_dict[2] = True

        for i in range(3, N+1):
            for j in range(1,i):
                if i % j == 0 and (not res_dict[i - j]):
                    res_dict[i] = True
                    break
                #res_dict[i] = False


        return res_dict[N]
