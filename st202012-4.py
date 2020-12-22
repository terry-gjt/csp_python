def floed(road,n):
    for temp in range(n):
        for i in range(n):
            if i==temp:
                break
            for j in range(n):
                if j == temp:
                    break
                tempnum=road[temp][j]+road[i][temp]
                if road[i][j]>tempnum:
                    road[i][j]=tempnum
def st4():
    allneednums=[]
    n,m,k=list(map(int,input().split()))
    roads=[]
    for i in range(n):
        neednums=list(map(int,input().split()))
        allneednums.append(neednums)
    for i in range(n-1):
        u,v,w = list(map(int, input().split()))
        roads[u][v]=w





st4()