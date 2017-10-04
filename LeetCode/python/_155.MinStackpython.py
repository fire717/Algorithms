# 对类的init还是不熟悉啊...

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.ms = []                             # 要这样声明
        self.mins = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.ms.append(x)
        if len(self.mins) == 0 or x<=self.mins[-1]:       #判断列表非空只能从长度么..我用==None报错了
            self.mins.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self.ms[-1] == self.mins[-1]:
            self.mins.pop()
        self.ms.pop()
        
        
    def top(self):
        """
        :rtype: int
        """
        return self.ms[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.mins[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
