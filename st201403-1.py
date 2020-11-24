# 相反数
def st201403_1():
    n = int(input())
    numbers=list(map(int,input().split(' ')))
    temp=0
    for num in numbers:
        if num*-1 in numbers:temp+=1
    print(temp//2)
if __name__ == '__main__':
    st201403_1()