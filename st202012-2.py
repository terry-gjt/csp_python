# 期末预测之最佳阈值 100分
def predict(y,a):
    if y<a:
        return 0
    else:
        return 1
def st20201202yuan():#70分 原先的解法
    m=int(input())
    y=0
    yAndResult=[]
    for i in range(m):
        listb=list(map(int,input().split()))
        yAndResult.append(listb)
    yAndResult.sort(key=takefirst)
    maxpredictnum=0
    maxpredictweight=0
    for a in yAndResult:
        predictnum=0
        for b in yAndResult:
            if b[1]==predict(b[0],a[0]):
                predictnum+=1
        if predictnum>maxpredictnum:
            maxpredictnum=predictnum
            maxpredictweight=a[0]
        elif predictnum==maxpredictnum:
            if a[0]>maxpredictweight:
                maxpredictweight=a[0]
    print(maxpredictweight)

def takefirst(elem):
    return elem[0]

def st20201202new():
    m=int(input())
    yAndResult={}
    for i in range(m):
        listb=list(map(int,input().split()))
        num=listb[0]
        temp=yAndResult.get(num, [0,0])#存入0和1的个数
        if listb[1]==0:
            temp[0]+=1
        else:
            temp[1]+=1
        yAndResult[num]=temp
    # yAndResult = {5: [2, 1], 2: [0, 1], 3: [1, 0], 4: [1, 0], 1000000: [0, 1], 1: [1, 0]}
    # yAndResult = {1: [1, 0], 2: [0, 1], 3: [1, 0], 4: [1, 0], 5: [2, 1] ,1000000: [0, 1]}
    yAndResultKeys=list(yAndResult.keys())
    yAndResultKeys.sort()
    beforeErrorNum = []
    behindErrorNum = []
    ErrorNum = []
    temp=0
    for i in yAndResultKeys:
        temp+=yAndResult[i][1]
        beforeErrorNum.append(temp)
    temp2 = 0
    for i in range(len(yAndResultKeys)-1,-1,-1):
        temp2+=yAndResult[yAndResultKeys[i]][0]
        behindErrorNum.append(temp2)
    behindErrorNum.reverse()
    # print(beforeErrorNum)
    # print(behindErrorNum)
    for i in range(len(beforeErrorNum)):
        ErrorNum.append(beforeErrorNum[i]+behindErrorNum[i])
    # print(ErrorNum)
    temp=0
    for i in range(1,len(ErrorNum)):
        if ErrorNum[temp]>=ErrorNum[i]:
            temp=i
    print(yAndResultKeys[temp])
st20201202new()