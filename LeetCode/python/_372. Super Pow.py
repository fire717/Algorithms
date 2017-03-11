#要实现还是很简单...然后我就超时了
#关键应该在那个对1337模运算上
class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        B=0
        l=len(b)
        for i in range(l):
            B+=b[i]*10**(l-i-1)
        return a**B%1337
        
        #或者这个更简洁：
        sb=''
        for x in b:
            sb+=str(x)
        B=int(sb)
        return a**B%1337
        
#AC..一行代码..便于学习 我改了下
#其实原理差不多，只是用到了reduce，lambda，学习下
class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        #return 0 if a % 1337 == 0 else pow(a, reduce(lambda x, y: (x * 10 + y) % 1140, b) + 1140, 1337)

        if a % 1337 == 0:
            return 0 
        else:
            return pow(a, reduce(lambda x, y: (x * 10 + y) % 1040, b) + 1040, 1337)
            #reduce()对list的每个元素反复调用函数f，并返回最终结果值。这里是对b中每个元素反复调用lambda
            #先计算b中头两个数，然后把结果和第三个数运算，再以此下去
            #lambda函数，参数为x,y 返回值为(x * 10 + y) % 1140
            #pow中有三个参数时，pow(x,y,z)：表示x的y次幂后除以z的余数
          ###问题来了，为啥要对1140取余然后加1140呢，测试了下不加1140是85ms，加了82ms，就是说提速了3ms...
            #目的应该是把最后的求余分散到之前简化运算量，同时减少空间复杂度。
            #而至于为什么选1140...我改成1240、1040居然都报错了
            #好吧，继续去看了解释：
            '''
            1337 only has two divisors 7 and 191 exclusive 1 and itself, so judge if a has a divisor of 7 or 191, and note that 7 and 191 are prime numbers, phi of them is itself - 1, then we can use the Euler's theorem, see it on wiki https://en.wikipedia.org/wiki/Euler's_theorem, it's just Fermat's little theorem if the mod n is prime.
            see how 1140 is calculated out:
                phi(1337) = phi(7) * phi(191) = 6 * 190 = 1140
            '''    
            #好像用到了欧拉定理...不管了，反正去掉1140也可以，先掌握能掌握的吧
            #熟悉reduce用法、lambda用法，及pow()三个参数的用法
