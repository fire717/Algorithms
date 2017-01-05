#初始解法，14/15时超时了...
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = len(numbers)
        ans = []
        i=0
        j=1
        flag = 1  #in case i,j be appended two times
        while numbers[i]+numbers[j]<target and j<l-1:
            while numbers[i]+numbers[j]<target and j<l-1:
                j+=1
            if numbers[i]+numbers[j]==target:
                ans.append(i+1)
                ans.append(j+1)
                flag=0
                break
            i+=1
            j=i+1
        if numbers[i]+numbers[j]==target and flag==1:
            ans.append(i+1)
            ans.append(j+1)
        return ans
        
#不厌其烦的修改...终于AC了...56ms-31.5%，比想象中稍好一点
#主要是要考虑有0的情况，而因为是升序，只要开始没0后面就不会有了，这里也卡了一会...
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = len(numbers)
        if numbers[0]==0:
            for x in range(1,l):
                if numbers[x]==target:
                    easyans=[1]
                    easyans.append(x+1)
                    return easyans
                if numbers[x]>target:
                    break
        ans = []
        i=0
        j=1            
        flag = 1  #in case i,j be appended two times
        while numbers[i]==0:
            i+=1
            j=i+1
        while numbers[i]+numbers[j]<target and j<l-1:
            while numbers[i]+numbers[j]<target and j<l-1:
                j+=1
            if numbers[i]+numbers[j]==target:
                ans.append(i+1)
                ans.append(j+1)
                flag=0
                break
            i+=1
            j=i+1
        if numbers[i]+numbers[j]==target and flag==1:
            ans.append(i+1)
            ans.append(j+1)
        return ans
