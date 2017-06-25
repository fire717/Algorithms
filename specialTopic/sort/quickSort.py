#coding:utf-8
originList = [3,1,4,1,5,9,2,6,5,3,5,8,9,7]

def quickSort(originList):
    if len(originList)<2:
        return originList
    i=0
    j=len(originList)-1
    a=originList[0]
    while i<j:
        while originList[j]>=a and i<j:
            j-=1
        while originList[i]<=a and i<j:
            i+=1
        if i<j:
            originList[i],originList[j]=originList[j],originList[i]
    originList[0],originList[i]=originList[i],originList[0]

    originList[:i] = quickSort(originList[:i])
    originList[i+1:] = quickSort(originList[i+1:])

    return originList

print quickSort(originList)
