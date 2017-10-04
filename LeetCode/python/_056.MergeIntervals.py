#我的思想比较简单粗暴
#设置一个x坐标，全0，然后把每一组元素判断，设为1，最后再输出
#但是在index上好像处理比较麻烦，过了test没有ac
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        lines = []
        start_num = 0 
        end_num = 0
        for line_range in intervals: #第一次遍历获取最大最小值
            start_num = min(start_num,line_range.start)
            end_num = max(start_num,line_range.end)
        ans = [0 for x in range(start_num,end_num+1)]
        print ans
        for line_range in intervals: #第二次遍历设置1
            start_index = line_range.start - start_num
            end_index = line_range.end - start_num
            ans[start_index:end_index] = [1 for x in range(end_index - start_index + 1)]
        print ans
        res = []    
        t = []
        for i in xrange(len(ans)): #第三次遍历输出 
            if ans[i] == 1 and len(t)==0:
                t.append(i+start_num)
            if ans[i] == 0 and len(t)==1:
                t.append(i+start_num-1)
                res.append(t)
                t = []
                
        return res
        
#刚听完浙大陈为老师讲座时间比较晚了，下午还有课，要去吃饭，先查吧
'''
Just go through the intervals sorted by start coordinate and 
either combine the current interval with the previous one if they overlap, 
or add it to the output by itself if they don't.
'''
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        out = []
        for i in sorted(intervals, key=lambda i: i.start): #自定义排序key函数
            if out and i.start <= out[-1].end:
                out[-1].end = max(out[-1].end, i.end)
            else:
                out += i,
        return out
