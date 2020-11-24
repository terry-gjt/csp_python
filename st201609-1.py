# 最大波动 在这几天中某天收盘价格与前一天收盘价格之差的绝对值最大是多少。
def st160901():
    n = int(input())
    numbers = list(map(int, input().split()))
    before=numbers[0]
    numbers.remove(before)
    temp=0
    for i in numbers:
        # print(i,abs(i-before),temp)
        if(abs(i-before)>temp):
            temp=abs(i-before)
        before=i
    print(temp)
if __name__ == '__main__':
    st160901()
