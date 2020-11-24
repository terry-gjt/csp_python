# 稀疏向量
def st200602():
    n, a,b = list(map(int, input().split()))
    u = {}
    sum=0
    for i in range(a):
        index, value = list(map(int, input().split()))
        u[index]=value
    for i in range(b):
        index, value = list(map(int, input().split()))
        sum+=u.get(index,0)*value
    print(sum)

if __name__ == '__main__':
    st200602()
