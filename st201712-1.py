# 最小差值
# 　　给定n个数，请找出其中相差（差的绝对值）最小的两个数，输出它们的差值的绝对值。
def st171201():
    n= int(input())
    numbers = list(map(int, input().split()))
    numbers.sort()
    # print(numbers)
    before=numbers[1]
    temp = abs(before-numbers[0])
    for i in numbers[2:]:
        # print(temp,before,i,abs(i-before))
        if abs(i-before) < temp:
            temp=abs(i-before)
        before=i
    print(temp)
if __name__ == '__main__':
    st171201()