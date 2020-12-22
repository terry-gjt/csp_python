
def st20201201():
    n=int(input())
    y=0
    for i in range(n):
        w,score=list(map(int,input().split()))
        y+=w*score
    if y>0:
        print(y)
    else:
        print(0)
st20201201()