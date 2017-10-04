#写了个比较暴力的，直接判断每个数是否有重复的位数，然后到n=7时超时了...看来还要继续想之前的方法了
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:return 1
        if n==1:return 10
        sameN=0
        maxN=10**n
        for i in range(11,maxN):
            t=[]
            while i>0:
                k=i%10
                i=i/10
                if k in t:
                    sameN+=1
                    break
                else:
                    t.append(k)
        return (maxN-sameN) 
#AC版本
#算了半天没有找出规律...还是查了
#论坛上这个，也是暴力法...
'''
For the first (most left) digit, we have 9 options (no zero); 
for the second digit we used one but we can use 0 now, so 9 options;
and we have 1 less option for each following digits. 
Number can not be longer than 10 digits.
'''
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        choices = [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        ans, product = 1, 1
        
        for i in range(n if n <= 10 else 10):
            product *= choices[i]
            ans += product
            
        return ans
