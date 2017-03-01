# 不懂队列又是怎么定义的.
# 好吧 queues...两个队列
# 但是查的这个解法也只有一个....就pop和top写的和我不一样，我直接写POP(0)，这里是循环便利一遍，最后的一个pop，前面的又append回去
# 可能与队列有关吧，但是如果定义成list，就x应该可以我那样操作啊...
class Stack(object):  
    def __init__(self):  
        """ 
        initialize your data structure here. 
        """  
        self.queue=[]  
  
    def push(self, x):  
        """ 
        :type x: int 
        :rtype: nothing 
        """  
        self.queue.append(x)  
  
    def pop(self):  
        """ 
        :rtype: nothing 
        """  
        for x in range(len(self.queue)-1):  
            self.queue.append(self.queue.pop())  
        self.queue.pop()  
  
    def top(self):  
        """ 
        :rtype: int 
        """  
        top=None  
        for x in range(len(self.queue)):  
            top=self.queue.pop()  
            self.queue.append(top)  
        return top  
              
  
    def empty(self):  
        """ 
        :rtype: bool 
        """  
        return len(self.queue)==0   #这个比我写的if简洁些，学习
