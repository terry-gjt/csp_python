# 碰撞的小球
BALLINDEX=0
def IntAndToList(s):
    global BALLINDEX
    num=int(s)
    BALLINDEX+=1
    return [num,1,BALLINDEX]
def takeFirst(elem):
    return elem[0]
def takeThird(elem):
    return elem[2]
def st180302():
    # n, L, t = 10,22,30
    # s='14 12 16 6 10 2 8 20 18 4'
    n,L,t = list(map(int, input().split()))
    balls = list(map(IntAndToList, input().split()))
    # balls = list(map(IntAndToList, s.split()))
    balls.sort(key=takeFirst)
    for i in range(t):
        for j in range(len(balls)):
            balls[j][0]+=balls[j][1]
            if balls[j][0]==0:
                balls[j][1]=1
            elif balls[j][0]==L:
                balls[j][1] = -1
            elif j>0:
                if balls[j][0]==balls[j-1][0]:
                    balls[j][1]*=-1
                    balls[j-1][1] *= -1
        # print(balls)
    balls.sort(key=takeThird)
    for ball in balls:
        print(ball[0],end=' ')
if __name__ == '__main__':
    st180302()