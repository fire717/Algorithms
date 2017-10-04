#没有按传统思维来做，本来想先求根号，然后加减来判断，但是太复杂
#于是想到了求质数时的做法，求因数，然后又想到了遍历一半，每次加i和n/i的做法
#46ms-53%
class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        son = [area,1]
        sqr = int(area**0.5)+1
        for i in xrange(2,sqr):
            if area % i == 0:
                son.append(i)
                son = [area/i] + son
        return [son[0],son[-1]]
