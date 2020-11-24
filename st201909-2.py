# 问题描述
# 小明种苹果2
def st191202():
    N=int(input())
    # N=4
    # strs=['4 74 -7 -12 -5',
    #       '5 73 -8 -6 59 -4',
    #       '5 76 -5 -10 60 -2',
    #       '5 80 -6 -15 59 0']
    trees=[]
    sum=0
    diaoluonum = 0
    for i in range(N):
        # l = list(map(int, strs[i].split()))
        l=list(map(int, input().split()))
        M=l[0]
        num=l[1]#第一个操作为统计数量
        diaoluo = False
        for j in range(2,M+1):#从第二个操作开始
            if l[j]>0 and l[j]<num:
                diaoluo=True
                num=l[j]
            elif l[j]<0:
                num+=l[j]
        if diaoluo:
            diaoluonum+=1
        sum += num
        # print(num,sum)
        trees.append(diaoluo)
    print(sum,end=' ')
    print(diaoluonum, end=' ')
    trees.append(trees[0])
    trees.append(trees[1])
    count=0
    for i in range(len(trees)-2):
        if trees[i] and trees[i+1] and trees[i+2]:
            count+=1
    print(count)
if __name__ == '__main__':
    st191202()