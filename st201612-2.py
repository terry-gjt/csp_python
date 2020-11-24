# 工资计算
def fun(n):
    temp = n + 3500
    sum = 0
    if n > 80000:
        sum += (n - 80000) * (1 - 0.45)
        n = 80000
    if n > 55000:
        sum += (n - 55000) * (1 - 0.35)
        n = 55000
    if n > 35000:
        sum += (n - 35000) * (1 - 0.30)
        n = 35000
    if n > 9000:
        sum += (n - 9000) * (1 - 0.25)
        n = 9000
    if n > 4500:
        sum += (n - 4500) * (1 - 0.20)
        n = 4500
    if n > 1500:
        sum += (n - 1500) * (1 - 0.10)
        n = 1500
    if n > 0:
        sum += (n) * (1 - 0.03)
    sum += 3500
    print(temp, "到手工资为", sum)

def st201612_2():
    n = int(input())
    num=0
    if n>61005:
        num=int(83500+(n-61005)/0.55)
    elif n>44755:
        num=int(58500 + (n - 44755) / 0.65)
    elif n>30755:
        num=int(38500 + (n - 30755) / 0.70)
    elif n>11255:
        num=int(12500 + (n - 11255) / 0.75)
    elif n>7655:
        num=int(8000 + (n - 7655) / 0.80)
    elif n>4955:
        num=int(5000 + (n - 4955) / 0.90)
    elif n>3500:
        num=int(3500 + (n - 3500) / 0.97)
    else:num=int(n)
    print(num)

if __name__ == '__main__':
    st201612_2()
    # fun(80000)
