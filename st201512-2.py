# 消除类游戏
def st151202():
    # n, m = 5, 8
    # pieces =[[2, 2, 3, 1, 2, 2, 2, 3],
    #          [3, 1, 1, 1, 1, 5, 5, 5],
    #          [2, 3, 2, 1, 3, 3, 2, 3],
    #          [2, 3, 2, 1, 3, 3, 2, 3],
    #          [2, 2, 3, 3, 3, 4, 5, 5]]
    # piecesAfter =[[2, 2, 3, 1, 2, 2, 2, 3],
    #               [3, 1, 1, 1, 1, 5, 5, 5],
    #               [2, 3, 2, 1, 3, 3, 2, 3],
    #               [2, 3, 2, 1, 3, 3, 2, 3],
    #               [2, 2, 3, 3, 3, 4, 5, 5]]
    n,m = list(map(int, input().split()))
    pieces=[]
    piecesAfter=[]
    for i in range(n):
        hang=list(map(int, input().split()))
        hang2=hang.copy()#浅复制，只能复制一维list
        pieces.append(hang)
        piecesAfter.append(hang2)
    # for a in piecesAfter:
    #     for b in a:
    #         print(b,end=' ')
    #     print()
    # print()
    for i in range(n):#遍历行
        temp = 1
        for j in range(1,m):
            if j==m-1:
                if pieces[i][j] == pieces[i][j - 1] and temp>=2:  # 相同就包括当前位置
                    for clearnum in range(j - temp, j+1):#当前位置之前temp个置零，包括当前位置
                        piecesAfter[i][clearnum]= 0
                elif temp>=3:
                    for clearnum in range(j - temp, j):#当前位置之前temp个置零，不包括当前位置
                        piecesAfter[i][clearnum]= 0
            if pieces[i][j] == pieces[i][j-1]:#相同就计数+1
                temp += 1
            elif temp >= 3 :#不同时，判断之前的相同个数是否大于3
                for clearnum in range(j - temp, j):#当前位置之前temp个置零，不包括当前位置
                    piecesAfter[i][clearnum]= 0
                temp=1
            else:
                temp=1
    for j in range(m):#遍历列
        temp = 1
        for i in range(1, n):
            if i == n - 1:
                if pieces[i][j] == pieces[i-1][j] and temp >= 2:  # 相同就包括当前位置
                    for clearnum in range(i - temp, i + 1):  # 当前位置之前temp个置零，包括当前位置
                        piecesAfter[clearnum][j] = 0
                elif temp >= 3:
                    for clearnum in range(i - temp, i):  # 当前位置之前temp个置零，不包括当前位置
                        piecesAfter[clearnum][j] = 0
            if pieces[i][j] == pieces[i-1][j]:  # 相同就计数+1
                temp += 1
            elif temp >= 3:  # 不同时，判断之前的相同个数是否大于3
                for clearnum in range(i - temp, i):  # 当前位置之前temp个置零，不包括当前位置
                    piecesAfter[clearnum][j] = 0
                temp = 1
            else:
                temp = 1
    for a in piecesAfter:
        for b in a:
            print(b,end=' ')
        print()
if __name__ == '__main__':
    st151202()