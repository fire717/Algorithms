#coding:utf-8

###自己按理解写的初版，能算出10时是15，但我发现中间的值和表对不上
items = ['a','b','c','d','e']
weight = [2,2,6,5,4]
value = [6,3,5,4,6]
t = {} #记录不同限重下的最大价值
for i in range(1,11):  #代表重量限制
    b=0
    for j in range(5):  #代表装几个东西
        if b:break #超重时直接break到外层
        if weight[j] > i:    #如果超过限重，直接break
            b=1
            break
        #如果没超重，分别比较加上当前物品和不加的价值差别
        if t.get(i-weight[j],0)+value[j] >= t.get(j-1,0):
            t[i]=t.get(i-weight[j],0)+value[j] 
        else:
            t[i]=t.get(j-1,0)
print t

#----------------------------------学习分界线------------------------------------#

###查的这个按照MIT编程导论课讲的写法
#写的真心好啊，又简洁。过段时间再回味下。
# -*- coding:utf-8 -*-
def fastmaxval(w,v,i,aw,m):
    #w：weight v：value i：物品个数 aw：allowable weight背包承受重量

    try: return m[(i, aw)]  #把(i,aw)当做key的值...表示从i个物品中选择满足能承受aw值的最大价值，因为是3元关系，所以用这样的dict
    except KeyError:  #当没有key时去读取m[key]就会报keyerror
        if i == 0:
            if w[i] <= aw:
                m[(i,aw)] = v[i]
                return v[i]
            else :
                m[(i,aw)] = 0
                return 0
        without_i = fastmaxval(w,v,i-1,aw,m) #计算不加入i的值
        if w[i] > aw:    #当第i个物品重量超过了可承受，直接return，因为这里是考虑了加入i的情况
            m[(i,aw)] = without_i
            return without_i
        else: #可放入i的情况
            with_i = v[i] + fastmaxval(w,v,i-1,aw-w[i],m) ###【关键！】我自己理解了来写代码的时候就是卡在这里了，还在想如何替换出来...
            #不需要考虑替换出哪一个，重新计算前i-1个最大的价值是多少就行了，而这里可以通过记录的字典来减少重复计算
            res = max(without_i,with_i)
            m[(i,aw)] = res
            return res

def maxval0(w,v,i,aw):
    m = {}
    return fastmaxval(w,v,i,aw,m)
##Test example
weights = [2, 2, 6, 5, 4]
vals = [6, 3, 5, 4, 6]
res = maxval0(weights, vals, len(vals)-1, 10)
print 'Fast Max Val =',res
