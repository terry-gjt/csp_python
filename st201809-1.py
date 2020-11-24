# 卖菜
def st180901():
    n = int(input())
    numbers = list(map(int, input().split()))
    numbers2=[]
    numbers2.append((numbers[0]+numbers[1])//2)
    i=1
    while i<n-1:
        numbers2.append((numbers[i-1] + numbers[i]+ numbers[i+1]) // 3)
        i+=1
    numbers2.append((numbers[n-2] + numbers[n-1]) // 2)
    for i in numbers2:print(i,end=' ')
if __name__ == '__main__':
    st180901()