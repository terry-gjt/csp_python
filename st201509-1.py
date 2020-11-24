# 问题描述
# 　　给定一个整数数列，数列中连续相同的最长整数序列算成一段，问数列中共有多少段？
def st150901():
    n = int(input())
    numbers=list(map(int, input().split()))
    temp=None
    num=0
    for i in numbers:
        if i!=temp:
            num+=1
            temp=i
    print(num)
if __name__ == '__main__':
    st150901()