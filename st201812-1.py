# 小明上学 红绿灯
def st181201():
    r,y,g = list(map(int, input().split()))
    sum=0
    n=int(input())
    for i in range(0,n):
        a,b = list(map(int, input().split()))
        if a==0:
            sum+=b
        elif a==1:
            sum+=b
        elif a==2:
            sum+=b+r
    print(sum)
if __name__ == '__main__':
    st181201()