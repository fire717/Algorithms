class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        x = []
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                x.append("FizzBuzz")
            elif i%3==0:
                x.append("Fizz")
            elif i%5==0:
                x.append("Buzz")
            else:
                x.append("%s" % i)
        return x
