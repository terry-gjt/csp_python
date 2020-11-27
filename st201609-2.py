# 火车购票
def st160902():
    n = int(input())
    # s='2 5 4 2'
    # numbers = list(map(int, s.split()))
    numbers = list(map(int, input().split()))
    seatgroup=[5]*20
    for num in numbers:
        havesell=False
        for i in range(len(seatgroup)):#先尽量相邻,第i+1排
            if seatgroup[i]>=num:
                for j in range(1,num+1):
                    print(i*5+5-seatgroup[i]+j,end=' ')
                seatgroup[i]-=num
                havesell=True
                break
        if havesell:
            pass
        else:#否则不相邻分配
            i=0
            while num!=0:
                if seatgroup[i] >= num:#这排就能坐下
                    for j in range(1, num + 1):
                        print(i * 5 + 5 - seatgroup[i] + j,end=' ')
                    seatgroup[i] -= num
                else:
                    for j in range(1, i * 5 + 6):#第i+1排最大值i*5+5
                        print(i * 5 + 5 - seatgroup[i] + j,end=' ')
                    seatgroup[i]=0
                    num -= seatgroup[i]
                    i+=1
        print()



if __name__ == '__main__':
    st160902()
