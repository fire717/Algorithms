# b不用循环和递归，好吧，还是要用math库，求对数...

import math
class Solution(object):
    def isPowerOfFour(self, num):
        if num <=0:
            return False
        a = math.log(num,4)
        if int(a) == a:
            return True
        else:
            return False
