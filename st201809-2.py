# 买菜
def st180901():
    n = int(input())
    hlist=[]
    wlist=[]
    for i in range(n):
        numbers = list(map(int, input().split()))
        hlist.append(numbers)
    for i in range(n):
        numbers = list(map(int, input().split()))
        wlist.append(numbers)
    # n=4
    # hlist=[[1, 3], [5, 6], [9, 13], [14, 15]]
    # wlist=[[2, 4], [5, 7], [10, 11], [13, 14]]
    i=0
    j=0
    time=0
    while i<n and j < n:
        # print(hlist[i],wlist[j],time)
        a=hlist[i][0]
        b=hlist[i][1]
        c = wlist[j][0]
        d = wlist[j][1]
        if a<=c and b>=c:
            if b>=d:
                time+=d-c
                j+=1
            else:
                time += b - c
                i += 1
        elif c<=a and d>=a:
            if d>=b:
                time+=b-a
                i+=1
            else:
                time += d - a
                j += 1
        elif a<=c:
            i+=1
        else:
            j+=1
    print(time)

if __name__ == '__main__':
    st180901()