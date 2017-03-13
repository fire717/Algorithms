#关键在于时间列表不止两个...#初始思路是写一个判断两个时间差的函数，然后分别遍历list中的任意两个从而求得最小值
#自己调试了很久，虽然写的很丑很长...然而提交时超时了...
class Solution(object):
    def comuteTwoTime(self,time1,time2):
        hour1 = int(time1[0:2])
        minu1 = int(time1[3:5])
        hour2 = int(time2[0:2])
        minu2 = int(time2[3:5])
        dist1 = 0
        dist2 = 0
        if minu1>minu2:
            if hour1>hour2:
                dist1 = (hour1-hour2)*60+(minu1-minu2)
                dist2 = (23+hour2-hour1)*60+(60+minu2-minu1)
            elif hour1<hour2:
                dist1 = (23+hour1-hour2)*60+(60+minu1-minu2)
                dist2 = (hour2-hour1-1)*60+(60+minu2-minu1)
            else:
                return minu1-minu2
        elif minu1<minu2:
            if hour1>hour2:
                dist1 = (hour1-hour2-1)*60+(60+minu1-minu2)
                dist2 = (23+hour2-hour1)*60+(60+minu2-minu1)
            elif hour1<hour2:
                dist1 = (23+hour1-hour2)*60+(60+minu1-minu2)
                dist2 = (hour2-hour1)*60+(minu2-minu1)
            else:
                return minu2-minu1
        else :
            return abs(hour1-hour2)*60
        return min(dist1,dist2)
        
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        l = len(timePoints)
        ans = 24*60
        for i in range(l-1):
            for j in range(i+1,l):
                distMinute = self.comuteTwoTime(timePoints[i],timePoints[j])
                if distMinute < ans:
                    ans = distMinute
        return ans

#好吧，论坛查的AC版本，简洁...
#Convert each timestamp to it's integer number of minutes past midnight, and sort the array of minutes.
#但是required minimum difference must be a difference between two adjacent elements in the circular array
               
class Solution(object):
    def convert(self,time):
        return int(time[:2]) * 60 + int(time[3:])  #好吧，才学的0不要写，last也不要写
    def findMinDifference(self, A):
        minutes = map(self.convert, A) 　#还是不熟悉吧..遍历list处理不需要for，用map()
        minutes.sort()
    
        return min( (y - x) % (24 * 60) 
                for x, y in zip(minutes, minutes[1:] + minutes[:1]) )      
                 #zip()接受任意多个（包括0个和1个）list作为参数，返回一个包list的tuple列表，
                 #minutes[1:] + minutes[:1]把循环列表整体左移一位
                 #但是这样怎么能计算出除了临近的两个之外的组合呢？额，minutes是排序了的...
                
                
