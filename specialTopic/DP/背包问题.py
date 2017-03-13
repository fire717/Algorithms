#coding:utf-8

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
