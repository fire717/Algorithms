#想到了用字典，但是是子母为key，不能比较，这里用数字做key就行了。而且字典也是无序的
#python字典 get()方法; 返回一个给定的key对应的值。如果key是没有用的，然后返回默认值None返回。
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        lp = len(p)  
        ls = len(s)  
          
        ds = {}  
        dp = {}  
          
        for i in s[:lp]:  
            ds[i] = ds.get(i,0) + 1  
        for i in p[:lp]:  
            dp[i] = dp.get(i,0) + 1  
             
        res = []  
        i = 0  
          
        while i < (ls-lp):  
            if dp == ds:  
                res.append(i),             #这里本来是写的res+=i，不知道为啥能执行....       
              
            ds[s[i]] -= 1  
            if ds[s[i]] == 0:  
                del ds[s[i]]  
            ds[s[i+lp]] = ds.get(s[i+lp],0) + 1  
            i+= 1  
        if ds == dp:  
            res.append(i),  
              
        return res  
