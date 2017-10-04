#恩，这是一道数学题..
#论坛查的
class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        a,b=x,y
        while y:
            r=x%y
            x=y
            y=r
        return bool(not z or (x and z<=a+b and not z%x))

#百度的思路: 1. z必须小于x, y的最大的一个.(这里应该是小于x+y吧) 2. z必须可以除尽x和y的最大公约数（gcd）. 、
#自己调试着写出来了，不过比上面那个要慢
class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if x>y:
            x,y = y,x
        if x+y==z or y==z or x==z:
            return True
        if z>y+x:
            return False
        if x==0:
            return False
        gy = 1
        for i in xrange(2,x+1):
            while x%i==0 and y%i==0:
                gy*=i
                x/=i
                y/=i
        if z%gy==0:
            return True
        else:
            return False
