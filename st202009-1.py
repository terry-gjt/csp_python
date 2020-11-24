# 　　称检测点查询
def takeSecond(elem):
    return elem[1]
def st2009_1():
    n,x,y=list(map(int,input().split()))
    all=[]
    for i in range(n):
        a,b = list(map(int,input().split()))
        d=(a-x)**2+(b-y)**2
        all.append([i+1,d])
    all.sort(key=takeSecond)
    for k in range(3):
        print(all[k][0])
if __name__ == '__main__':
    st2009_1()
