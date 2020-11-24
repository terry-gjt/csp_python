#给出读者的来访记录，请问每一条记录中的读者是第几次出现。
def st141201():
    n = int(input())
    numbers=list(map(int, input().split()))
    times={}
    for number in numbers:
        if number in times:
            times[number]+=1
            print(times[number], end=' ')
        else:
            print(1, end=' ')
            times[number]=1
if __name__ == '__main__':
    st141201()