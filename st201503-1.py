# 　　旋转是图像处理的基本操作，在这个问题中，你需要将一个图像逆时针旋转90度。
def st150301():
    m,n = list(map(int,input().split()))
    numbersarray = []
    for i in range(0, m):
        numbersarray.append(list(map(int, input().split())))
    # print(numbersarray)
    for x in range(n-1,-1,-1):
        for y in range(0, m):
            print(numbersarray[y][x],end=' ')
        print()

if __name__ == '__main__':
    st150301()