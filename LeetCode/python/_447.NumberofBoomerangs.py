# 貌似是没读懂题然后想复杂了。。。

class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        p = points  
        res = 0  
        for i in xrange(len(p)):        #注意xrange() 比range效率高。使用xrange()进行遍历，每次遍历只返回一个值。只需一个参数，默认0开始
            dic = {}  
            for j in xrange(len(p)):  
                dist = (p[j][1] - p[i][1])**2 +  (p[j][0] - p[i][0])**2  #题中说pairwise distinct意思是只有两排吗，看这里是
                dic[dist] = dic.get(dist,0) +1               #dict.get(key, default=None)返回指定键的值，【如果值不在字典中返回default值】
            #print dic  
            for i in dic.values():  
                if i > 1:  
                    res += i*(i-1)  
        return res  
