
#果然想的太简单了。初始版
class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        strs.sort(key=len)
        ans = 0
        for i in strs:
            if i.count('0')<=m and i.count('1')<=n:
                ans+=1
                m-=i.count('0')
                n-=i.count('1')
            if m<=0 and n <=0:
                return ans
        return ans
        
  
  
  #查了下，说类似于0-1背包问题
 '''
 dp(k, x, y) is the maximum strs we can include when we have x zeros, y ones and only the first k strs are considered.

dp(len(strs), M, N) is the answer we are looking for

I first implemented a dfs + memoization, which gets MLE, so I created a bottom up style dp.
With bottom up, we can use something called "rolling array" to optimize space complexity from O(KMN) to O(MN)
 '''
  class Solution(object):
    def findMaxForm(self, strs, m, n):
        
        dp = [[0] * (n+1) for _ in range(m+1)]
        
        def count(s):
            return sum(1 for c in s if c == '0'), sum(1 for c in s if c == '1')
        
        for z, o in [count(s) for s in strs]:
            for x in range(m, -1, -1):
                for y in range(n, -1, -1):
                    if x >= z and y >= o:
                        dp[x][y] = max(1 + dp[x-z][y-o], dp[x][y])
                        
        return dp[m][n]
