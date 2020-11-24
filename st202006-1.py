# 　　线性二分类器
def st200601():
    n,m = list(map(int,input().split()))
    dians=[]
    xians=[]
    for i in range(n):
        dians.append(input().split())
    for i in range(m):
        xians.append(list(map(int, input().split())))
    # 测试输入
    # dians = [['1','1','A'],
    #          ['1', '0', 'A'],
    #          ['1', '-1', 'A'],
    #          ['2', '2', 'B'],
    #          ['2', '3', 'B'],
    #          ['0', '1', 'A'],
    #          ['3', '1', 'B'],
    #          ['1', '3', 'B'],
    #          ['2', '0', 'A'],
    #          ['1', '1', 'A']]
    # xians = [[0, 2, -3],
    #          [-3,0,2],
    #          [-3,1,1]]
    for xian in xians:
        class1 = [False, dians[0][2]]
        temp=xian[0] + int(dians[0][0]) * xian[1] + int(dians[0][1]) * xian[2]
        if temp > 0:#点不会在线上，故不考虑
            class1[0] = True
        for dian in dians:
            temp=xian[0] + int(dian[0]) * xian[1] + int(dian[1]) * xian[2]
            if (temp > 0)==class1[0]:
                if dian[2]!=class1[1]:
                    print('No')
                    break
            elif (temp < 0)==class1[0]:
                if dian[2]==class1[1]:
                    print('No')
                    break
        else:print('Yes')

if __name__ == '__main__':
    st200601()
