#First we find the first two valid numbers and generate a fibonacci like string use these two numbers.
#Then compare the generated string with the given num string.

class Solution(object):
    def isAdditiveNumber(self, num):
        if len(num) < 3:
            return False
        for i in range(len(num) // 2):
            for j in range(i+1, len(num) // 3 * 2):
                one = int(num[:i+1])
                two = int(num[i+1:j+1])  #取得前两个数
                if self.generate_fib_str(one, two, len(num)) == num:
                    return True
                if num[j] == 0:
                    break
            if num[0] == '0':
                break
        return False
    
    def generate_fib_str(self, a, b, n): #生成了拿去比较
        # type: int, int, int -> str
        fib_str = str(a) + str(b)
        while len(fib_str) < n:
            fib_str += str(a + b)  #恩 比较好理解
            a, b = b, a+b
        return fib_str[:n]
