# 跳一跳 1表示此次跳跃跳到了方块上但是没有跳到中心，2表示此次跳跃跳到了方块上并且跳到了方块中心，
def st180301():
    numbers = list(map(int, input().split()))
    temp=2
    score=0
    for i in numbers:
        if i==2:
            score+=temp
            temp+=2
        elif i==1:
            score+=1
            temp=2
        elif i==0:
            break
    print(score)
if __name__ == '__main__':
    st180301()