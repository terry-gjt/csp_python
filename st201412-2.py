# 问题描述
# 　　在图像编码的算法中，需要将一个给定的方形矩阵进行Z字形扫描(Zigzag Scan)。
# 　　对于下面的4×4的矩阵，
# 　　1 5 3 9
# 　　3 7 5 6
# 　　9 4 6 4
# 　　7 3 1 3
# 　　对其进行Z字形扫描后得到长度为16的序列：
# 　　1 5 3 9 7 3 9 5 4 7 3 6 6 4 1 3
# 　　请实现一个Z字形扫描的程序，给定一个n×n的矩阵，输出对这个矩阵进行Z字形扫描的结果。
# 输入格式
# 　　输入的第一行包含一个整数n，表示矩阵的大小。
# 　　输入的第二行到第n+1行每行包含n个正整数，由空格分隔，表示给定的矩阵。
# 输出格式
# 　　输出一行，包含n×n个整数，由空格分隔，表示输入的矩阵经过Z字形扫描后的结果。
# 样例输入
# 4
# 1 5 3 9
# 3 7 5 6
# 9 4 6 4
# 7 3 1 3
# 样例输出
# 1 5 3 9 7 3 9 5 4 7 3 6 6 4 1 3
# 评测用例规模与约定
# 　　1≤n≤500，矩阵元素为不超过1000的正整数。
def st2():
    n = int(input())
    numbersarray=[]
    for i in range(0,n):
        numbersarray.append(list(map(int,input().split())))
    # numbersarray=[[1,5,3,9],[3,7,5,6],[9,4,6,4],[7,3,1,3]]
    # n=4
#输出顺序
    # 00            p=0 x=0 p-x=0
    # 01 10         p=1
    # 20 11 02      p=2
    # 03 12 21 30   p=3
    # 31 22 13      p=4
    # 23 32         p=5
    # 33 ----60 51 42 33 24 15 06
    for p in range(0, n*2-1):
        if(p%2!=0):
            for x in range(0, p+1):
                # print('111:', p, x,p-x)
                if(p-x>=0 and p-x<n and x<n):
                    # print('222:',p,x,p-x)
                    print(numbersarray[x][p-x],end=' ')
        else:
            for x in range(0, p+1):
                # print('333:', p,p-x, x)
                if(p-x>=0 and p-x<n and x<n):
                    # print('444:', p,p-x, x)
                    print(numbersarray[p-x][x],end=' ')

if __name__ == '__main__':
    st2()