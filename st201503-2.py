# 数字排序
def takeSecond(elem):
    return elem[1]
def st150302():
    n=int(input())
    nums= list(map(int,input().split()))
    nums.sort()
    result=[]
    count=1
    for i in range(1,n):
        if nums[i]==nums[i-1]:
            count+=1
        else:
            result.append([nums[i-1],count])
            count=1
    result.append([nums[n-1], count])
    result.sort(key=takeSecond,reverse=True)
    for temp in result:
        print(temp[0],end=' ')
        print(temp[1])
if __name__ == '__main__':
    st150302()