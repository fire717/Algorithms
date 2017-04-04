#不用乘除和模运算实现除法
class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        positive = (dividend < 0) is (divisor < 0)#这是啥。。 p为True则同号，false异号
        #is判断的是a对象是否就是b对象，是通过id来判断的
        #==判断的是a对象的值是否和b对象的值相等，是通过value来判断的
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1  #通过移位操作吧
                temp <<= 1
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)
