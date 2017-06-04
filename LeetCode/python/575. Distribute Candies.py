#TLE了。
class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        same = []
        count = 0
        for i in candies:
            if i not in same:
                count+=1
                same.append(i)
        half = len(candies)/2
        if half<=count:
            return half
        else:
            return count
            
  #想到直接用集合，AC了。但是这道题好像还看不到时间。。。
  #很神奇，有空研究下python set()实现原理
class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        same = set(candies)
        count = len(same)
        half = len(candies)/2
        if half<=count:
            return half
        else:
            return count
