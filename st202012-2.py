#70分 等系统放出题目了再优化一下
def takefirst(elem):
    return elem[0]
def takesecond(elem):
    return elem[1]
def predict(y,a):
    if y<a:
        return 0
    else:
        return 1
def st20201202():
    m=int(input())
    y=0
    yandresult=[]
    for i in range(m):
        listb=list(map(int,input().split()))
        yandresult.append(listb)
    maxpredictnum=0
    maxpredictweight=0
    for a in yandresult:
        predictnum=0
        for b in yandresult:
            if b[1]==predict(b[0],a[0]):
                predictnum+=1
        if predictnum>maxpredictnum:
            maxpredictnum=predictnum
            maxpredictweight=a[0]
        elif predictnum==maxpredictnum:
            if a[0]>maxpredictweight:
                maxpredictweight=a[0]
    print(maxpredictweight)
st20201202()