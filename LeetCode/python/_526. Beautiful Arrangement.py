#没思路 也不知道怎么暴力解。。
#Python recursion + DP 66ms
#Save the pre-computed the result globally and reuse.


cache={}
class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        def helper(i, X):
            if i == 1:
                return 1
            key = (i, X) #cache保存已算过的
            if key in cache:
                return cache[key]
            total = 0 #表组合数
            for j in xrange(len(X)):
                if X[j] % i == 0 or i % X[j] == 0:  #若当前位置满足
                    total += helper(i - 1, X[:j] + X[j + 1:]) #递归  在考虑去掉当前位置的组合数
            cache[key] = total
            return total
        return helper(N, tuple(range(1, N + 1)))
        
