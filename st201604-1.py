# 折点计数 计算有几个折点
def st160401():
    n = int(input())
    numbers = list(map(int, input().split()))
    if(n<3):
        print(0)
        return
    a=numbers[0]
    b=numbers[1]
    numbers.remove(a)
    numbers.remove(b)
    num=0
    for i in numbers:
        if (a > b and b < i):
            # print(b, end=' ')
            num+=1
        if (a < b and b > i):
            # print(b, end=' ')
            num += 1
        a=b
        b=i
    print(num)
if __name__ == '__main__':
    st160401()
