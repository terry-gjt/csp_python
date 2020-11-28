# 俄罗斯方块
def st160402():
    # s=['0 0 0 0 0 0 0 0 0 0',
    #    '0 0 0 0 0 0 0 0 0 0',
    #    '0 0 0 0 0 0 0 0 0 0',
    #    '0 0 0 0 0 0 0 0 0 0',
    #    '0 0 0 0 0 0 0 0 0 0',
    #    '0 0 0 0 0 0 0 0 0 0',
    #    '0 0 0 0 0 0 0 0 0 0',
    #    '0 0 0 0 0 0 0 0 0 0',
    #    '0 0 0 0 0 0 0 0 0 0',
    #    '0 0 0 0 0 0 0 0 0 0',
    #    '0 0 0 0 0 0 0 1 0 0',
    #    '0 0 0 0 0 0 1 0 0 0',
    #    '0 0 0 0 0 0 1 0 0 0',
    #    '1 1 1 0 0 0 1 1 1 1',
    #    '0 0 0 0 1 0 0 0 0 0']
    # s2 = ['0 0 0 0',
    #      '0 1 1 1',
    #      '0 0 0 1',
    #      '0 0 0 0']
    # n=3
    space=[]
    fangge=[]
    fanggeindex={}#方格每列的最低位置
    spaceindex={}#空间其中4列的最高位置
    for j in range(15):
        # hang = list(map(int, s[j].split()))
        hang = list(map(int, input().split()))
        space.append(hang)
    for a in range(4):
        # hang = list(map(int, s2[a].split()))
        hang = list(map(int, input().split()))
        fangge.append(hang)
    n = int(input())
    # print(fangge)
    for j in range(n-1, 3+n):#计算空间其中4列的最高位置
        spaceindex[j] = 15
        for i in range(14, -1, -1):
            if space[i][j]==1:
                spaceindex[j]=i
    for j in range(4):#计算方格每列的最低位置
        for i in range(4):
            if fangge[i][j]==1:
                fanggeindex[j]=i
    minhigh=14#4列中取最小下落距离，最大为14
    for index in fanggeindex:
        high=spaceindex[index+n-1]-fanggeindex[index]-1
        if high<minhigh:
            minhigh=high
    for i in range(4):
        for j in range(4):
            if fangge[i][j]==1:
                space[i+minhigh][n +j-1] = 1
                # print(i+minhigh,n+j)
    for hang in space:
        for temp in hang:
            print(temp,end=' ')
        print()
    # print(fanggeindex)
    # print(spaceindex)
if __name__ == '__main__':
    st160402()
