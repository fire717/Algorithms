#这种题感觉没啥思路，只能一个个条件写
#写成这样，题目中几个都满足了。但是提交时遇到01循环的还是不行。。
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        ans=str(float(numerator)/float(denominator))[:10]
        t = 0
        for i in xrange(len(ans)-1):
            if ans[i] != ans[i+1]:
                continue
            else:
                t+=1
            if t==3:
                k = '(%s)' % ans[i]  
                ans = ans[:i-2]+k
                break
        return ans
        

#好像用到了栈
class Solution:
    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        n, remainder = divmod(abs(numerator), abs(denominator))
        #divmod(a,b)方法返回的是a//b（除法取整）以及a对b的余数 / 返回结果类型为tuple
        sign = '-' if numerator*denominator < 0 else ''
        result = [sign+str(n), '.']
        stack = []
        while remainder not in stack:
            stack.append(remainder)
            n, remainder = divmod(remainder*10, abs(denominator))
            result.append(str(n))

        idx = stack.index(remainder)
        result.insert(idx+2, '(')
        result.append(')')
        return ''.join(result).replace('(0)', '').rstrip('.')
        # rstrip() 删除 string 字符串末尾的指定字符（默认为空格）.语法str.rstrip([chars])
