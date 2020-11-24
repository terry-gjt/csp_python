# 小中大
def st190301():
    n = int(input())
    numbers=list(map(int,input().split()))
    if numbers[0]>numbers[n-1]:
        max=numbers[0]
        min=numbers[n-1]
    else:
        max=numbers[n-1]
        min=numbers[0]
    print(max,end=' ')
    if n%2==0:
        zhong=(numbers[n//2-1]+numbers[n//2])
        if zhong%2==0:
            print(zhong//2, end=' ')
        else:
            print(zhong/2, end=' ')
    else:
        print(numbers[n//2], end=' ')
    print(min)

if __name__ == '__main__':
    st190301()

