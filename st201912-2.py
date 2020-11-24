# 回收站选址
def st191202():
    n=int(input())
    dians=[]
    num=[0,0,0,0,0]
    for i in range(n):
        dians.append(list(map(int, input().split())))
    # print(dians)
    for dian in dians:
        x = dian[0]
        y = dian[1]
        temp = 0 #当前点四个对角垃圾数
        if [x, y + 1] in dians and [x, y - 1] in dians and [x + 1, y] in dians and [x - 1, y] in dians:
            if [x + 1, y + 1] in dians:
                temp += 1
            if [x + 1, y - 1] in dians:
                temp += 1
            if [x - 1, y + 1] in dians:
                temp += 1
            if [x - 1, y - 1] in dians:
                temp += 1
            if temp == 0:
                num[0] += 1
            elif temp == 1:
                num[1] += 1
            elif temp == 2:
                num[2] += 1
            elif temp == 3:
                num[3] += 1
            elif temp == 4:
                num[4] += 1
    for i in num:
        print(i)

if __name__ == '__main__':
    st191202()