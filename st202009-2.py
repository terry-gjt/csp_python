# 　　风险人群筛查
def Inarea(x,y,x1,y1,x2,y2):
    if x>=x1 and x<=x2 and y>=y1 and y<=y2:
        # print(x,y,'in')
        return True
    else:
        # print(x, y, 'out')
        return False
def st2009_2():
    # s='5 2 6 20 40 100 80'
    # n, k, t, x1, y1, x2, y2 = list(map(int, s.split()))
    s2 = ['100 80 100 80 100 80 100 80 100 80 100 80',
          '60 50 60 46 60 42 60 38 60 34 60 30',
          '10 60 14 62 18 66 22 74 26 86 30 100',
          '90 31 94 35 98 39 102 43 106 47 110 51',
          '0 20 4 20 8 20 12 20 16 20 20 20']
    n,k,t,x1,y1,x2,y2=list(map(int,input().split()))
    jinduo=0
    douliu=0
    for i in range(n):
        # weizhi = list(map(int, s2[i].split()))
        weizhi=list(map(int,input().split()))
        temp=False
        thismentimes = 0
        for j in range(len(weizhi) // 2):
            if Inarea(weizhi[j * 2],weizhi[j * 2+1],x1,y1,x2,y2):
                temp=True
                thismentimes+=1
                if thismentimes >= k:
                    douliu += 1
                    break
            else:thismentimes=0
        if temp:jinduo+=1

    print(jinduo)
    print(douliu)

if __name__ == '__main__':
    st2009_2()

