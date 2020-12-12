# Z字形扫描
def st2():
    n = int(input())
    numbersarray=[]
    for i in range(0,n):
        numbersarray.append(list(map(int,input().split())))
    # numbersarray=[[1,5,3,9],[3,7,5,6],[9,4,6,4],[7,3,1,3]]
    # n=4
#输出顺序
    # 00            p=0 x=0 p-x=0
    # 01 10         p=1
    # 20 11 02      p=2
    # 03 12 21 30   p=3
    # 31 22 13      p=4
    # 23 32         p=5
    # 33 ----60 51 42 33 24 15 06
    for p in range(0, n*2-1):
        if(p%2!=0):
            for x in range(0, p+1):
                # print('111:', p, x,p-x)
                if(p-x>=0 and p-x<n and x<n):
                    # print('222:',p,x,p-x)
                    print(numbersarray[x][p-x],end=' ')
        else:
            for x in range(0, p+1):
                # print('333:', p,p-x, x)
                if(p-x>=0 and p-x<n and x<n):
                    # print('444:', p,p-x, x)
                    print(numbersarray[p-x][x],end=' ')

if __name__ == '__main__':
    st2()