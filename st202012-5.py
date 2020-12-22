# 最后几分钟做的，没来得及提交，不知道几分
def st5():
    n,m=int(input())
    dongli={}
    for i in range(m):
        listb=list(map(int,input().split()))
        L=listb[1]
        R=listb[2]
        if listb[0]==1:
            for i in range(L,R+1):
                dongli[i]=dongli.get(i,[0,0,0])
                dongli[i][0]+=listb[3]
                dongli[i][1] += listb[4]
                dongli[i][2] += listb[5]
        elif listb[0]==2:
            for i in range(L,R+1):
                dongli[i]=dongli.get(i,[0,0,0])
                dongli[i][0] *= listb[3]
                dongli[i][1] *= listb[3]
                dongli[i][2] *= listb[3]
        elif listb[0]==3:
            for i in range(L,R+1):
                dongli[i]=dongli.get(i,[0,0,0])
                dongli[i][0] *= listb[4]
                dongli[i][1] *= listb[5]
                dongli[i][2] *= listb[3]
        elif listb[0]==4:
            sum=0
            for i in dongli:
                sum+=(dongli[i]**2)
                # sum=sum%1000000007
            print(sum)

st5()