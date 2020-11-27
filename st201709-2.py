# 公共钥匙盒
def takeFirst(elem):
    return elem[0]
def takeSecond(elem):
    return elem[1]
def takeThird(elem):
    return elem[2]
def st170901():
    n,k = list(map(int, input().split()))
    # n,k=5,7
    # s=['1 1 14',
    #    '3 3 12',
    #    '1 15 12',
    #    '2 7 20',
    #    '3 18 12',
    #    '4 21 19',
    #    '5 30 9']
    keys=[]
    for j in range(1,n+1):
        keys.append(j)
    uses=[]
    for i in range(k):
        # use = list(map(int, s[i].split()))
        use= list(map(int, input().split()))
        uses.append([use[0],use[1],True])#钥匙编号，时间，取走或放回
        uses.append([use[0], use[1]+use[2], False])
    uses.sort(key=takeFirst)  # 第三关键字，放回要从小到大
    uses.sort(key=takeThird)#第二关键字，先放再拿
    uses.sort(key=takeSecond)#第一关键字，时间
    # print(uses)
    for u in uses:
        if u[2]:
            keys[keys.index(u[0])]=0#取走钥匙，即设为0
            # print(keys)
        else:
            keys[keys.index(0)] = u[0]  # 放回钥匙，设为钥匙编号
            # print(keys)
    for key in keys:
        print(key,end=' ')

if __name__ == '__main__':
    st170901()