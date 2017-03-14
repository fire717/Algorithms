#出自麻省理工学院公开课：计算机科学及编程导论-13动态规划,重叠的子问题,最优子结构
#自己照着模糊的视频敲的...
#coding:utf-8

def fib(n):
    global numCalls
    numCalls += 1
    print 'fib called with',n
    if n<=1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

#快速求法
def fastFib(n,memo):
    global numCalls
    numCalls += 1
    print 'fib1 called with',n
    if n not in memo:       #用dict存储计算过一次的数
        memo[n]=fastFib(n-1,memo)+fastFib(n-2,memo)
    return memo[n]

def fib1(n):
    memo={0:0,1:1}
    return fastFib(n,memo)

if __name__=='__main__':#表示执行的是此代码所在的文件。 如果这个文件是作为模块被其他文件调用，不会执行这里面的代码。 只有执行这个文件时， if 里面的语句才会被执行。 这个功能经常可以用于进行测试。
    numCalls = 0
    n = 6
    res = fib1(n)
    print 'fib of', n, '=' ,res,'numCalls =',numCalls
