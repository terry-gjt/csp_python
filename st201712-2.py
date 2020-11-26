# 游戏 k的倍数或其末位数（即数的个位）为k就淘汰
def st171201():
    n,k = list(map(int, input().split()))
    # n,k=5,2
    chirdren=[True]*n
    outnum=0
    num=1#报的数
    index=0#当前位置
    while outnum<n:
        if chirdren[index]:
            if num%k==0 or num%10==k:
                chirdren[index]=False
                outnum+=1
                if outnum==n:
                    print(index+1)
                # print(index+1,num,'out')
            num += 1
        if index==n-1:
            index=0
        else:
            index+=1

if __name__ == '__main__':
    st171201()