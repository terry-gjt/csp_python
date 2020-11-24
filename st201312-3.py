# 最大的矩形 100分
def st201312_3():
    n = int(input())
    nums = list(map(int, input().split()))
    # n=6
    # nums=[3, 1, 6, 5, 2, 3]
    result=[]
    for i in range(n):
        high=nums[i]
        temp = 0
        for a in range(i,-1,-1):
            if nums[a]>=high:
                temp+=1
            else:
                break
        for a in range(i,n):
            if nums[a]>=high:
                temp+=1
            else:
                break
        result.append(temp*high-high)
    # print(result)
    print(max(result))

if __name__ == '__main__':
    st201312_3()