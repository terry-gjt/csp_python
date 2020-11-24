# 问题描述
# 小明种苹果
def st190901():
    N,M = list(map(int, input().split()))
    trees=[]
    sum=0
    for i in range(N):
        l=list(map(int, input().split()))
        l2=[i]
        sum+=l[0]
        num=0
        for j in range(1,M+1):
            num+=l[j]
        sum += num
        l2.append(num)
        # l2.append(i)
        trees.append(l2)
    print(sum,end=' ')
    trees.sort(key=lambda x:x[1])
    # print(trees)
    print(trees[0][0]+1,end=' ')
    print(trees[0][1]*-1,end=' ')
if __name__ == '__main__':
    st190901()