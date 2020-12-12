# 画图
# 输入格式
# 　　输入的第一行包含一个整数n，表示要画的矩形的个数。
# 　　接下来n行，每行4个非负整数，分别表示要画的矩形的左下角的横坐标与纵坐标，以及右上角的横坐标与纵坐标。
# 输出格式
# 　　输出一个整数，表示有多少个单位的面积被涂上颜色。
# 样例输入
# 2
# 1 1 4 4
# 2 3 6 5
# 样例输出
# 15
# 评测用例规模与约定
# 　　1<=n<=100，0<=横坐标、纵坐标<=100。
def st1():
    n = int(input())
    d={}
    windows = []
    for i in range(0, n):
        windows.append(list(map(int, input().split())))
    for window in windows:
        for x in range(window[0], window[2]):
            for y in range(window[1], window[3]):
                d[x*100+y]=True
    print(len(d))
if __name__ == '__main__':
    st1()