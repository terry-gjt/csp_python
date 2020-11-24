# 　　给定n个不同的整数，问这些数中有多少对整数，它们的值正好相差1。
def st140901():
    n = int(input())
    numbers=list(map(int,input().split()))
    temp=0
    for num in numbers:
        if num+1 in numbers:temp+=1
    print(temp)
if __name__ == '__main__':
    st140901()