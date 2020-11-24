# 　　给定一个十进制整数n，输出n的各位数字之和。
def st151201():
    n = input()
    sum=0
    for i in n:
        sum=sum+int(i)
    print(sum)
if __name__ == '__main__':
    st151201()