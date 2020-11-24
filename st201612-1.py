# 中间数
# 　　在一个整数序列a1, a2, …, an中，如果存在某个数，大于它的整数数量等于小于它的整数数量，则称其为中间数。在一个序列中，可能存在多个下标不相同的中间数，这些中间数的值是相同的。

def st161201():
    n = int(input())
    numbers = list(map(int, input().split()))
    numbers.sort()
    if(len(numbers)%2==0):
        if(numbers[len(numbers)//2-1]!=numbers[len(numbers)//2]):
            print(-1)
            return
    before=0
    after=0
    temp = numbers[len(numbers) // 2]
    for i in numbers:
        if(i<temp):
            before+=1
        elif(i>temp):
            after+=1
    if(before==after):print(temp)
    else:print(-1)
if __name__ == '__main__':
    st161201()
