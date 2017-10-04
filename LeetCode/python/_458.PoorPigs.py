#????测试的时候，1000篮子那个答案居然是5？只要5头猪能找出1000篮子中有毒的？？？
#黑人问号？难道我是猪？如果要靠运气，那不是1头猪就可以？？？？？？

#看了一个例子，原来还可以两头猪单独喝一篮子，然后一起喝一篮子！这样两个都挂了也能知道...
#这样的话，可以用不同数量指代不同篮子了...
#这样类似2进制了

#应该最后一次喝水要在测试时间一半

#同一个猪分不同轮次喝水，按死亡时间也能判断出不同篮子！

class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        states = minutesToTest / minutesToDie + 1

        return int(math.ceil(math.log(buckets, states)))



