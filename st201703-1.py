# 分蛋糕
def st170301():
    n,k = list(map(int,input().split()))
    numbers=list(map(int, input().split()))
    temp=0
    num=0
    for i in numbers:
        temp+=i
        if temp>=k:
            # print(temp)
            temp=0
            num+=1
    if temp==0:
        print(num)
    else:
        print(num+1)
if __name__ == '__main__':
    st170301()