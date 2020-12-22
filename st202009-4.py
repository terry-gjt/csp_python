# 星际旅行
# 参考自https://blog.csdn.net/weixin_44310435/article/details/108707450
# 原来是55分
import math
from math import sqrt, acos, cos

#两点距离
def distance(p1, p2) -> float:
    ans = 0.0
    for i in range(n):
        ans += (p1[i] - p2[i])**2
    return sqrt(ans)

# 重要的公式
def getdis(i, j) -> float:
    p1, p2 = point[i], point[j]
    AB_mold = distance(p1, p2)
    # 都在边缘上
    if edge[i] and edge[j]:
        # 求劣弧角度即可
        aerfa = 2 * math.asin((AB_mold / 2) / r)
        return aerfa * r
    else:
        AO_mold = distance(p1, heidong)
        BO_mold = distance(p2, heidong)
        cosA = (AO_mold**2 + AB_mold**2 - BO_mold**2) / (2 * AO_mold * AB_mold)
        cosB = (BO_mold**2 + AB_mold**2 - AO_mold**2) / (2 * BO_mold * AB_mold)
        # cosA = pi-r/AO_mold
        # cosB = pi-r/BO_mold

        # A、B两点的连线不经过黑洞，直接返回两者距离，角为钝角或直角
        if cosA < 0 or cosB < 0 or abs(cosA - 0) < 1e-7 or abs(cosB - 0) < 1e-7:
            return AB_mold
        # A、B两点的连线经过黑洞
        else:
            # h是黑洞中心到AB连线的距离
            h = AO_mold * (sqrt(1 - cosA**2))  #sinA，三角函数
            if h >= r:
                return AB_mold
            # 最麻烦的情况，AB两点均在黑洞外且连线经过黑洞
            else:
                cosO = (AO_mold**2 + BO_mold**2 - AB_mold**2) / (2 * AO_mold * BO_mold)
                # E，F点分别为A，B两点在边缘上的切点
                # 如果有一个点在边缘上，那么可以少计算一些
                if edge[i]:
                    AE_mold = 0
                    FB_mold = sqrt(BO_mold**2 - r2)
                    beta = acos(cosO) - acos(r / BO_mold)
                elif edge[j]:
                    FB_mold = 0
                    AE_mold = sqrt(AO_mold**2 - r2)
                    beta = acos(cosO) - acos(r / AO_mold)
                # 两点都不在边缘上
                else:
                    AE_mold = sqrt(AO_mold**2 - r2)
                    FB_mold = sqrt(BO_mold**2 - r2)
                    # beta = acos(cosO) - pi - (acos(r / AO_mold) + acos(r / BO_mold))
                    beta = acos(cosO) - (acos(r / AO_mold) + acos(r / BO_mold))
                    # print(i,j,'都不在edge')
                EF_arc = beta * r
                return EF_arc + FB_mold + AE_mold


if __name__ == "__main__":
    # n维, m个点
    n, m = map(int, input().split())
    # 半径
    r = int(input())
    r2 = r * r
    # 黑洞信息
    heidong = tuple(map(int, input().split()))
    point = [None] * m  #初始化点
    edge = [False] * m  #是否在黑洞边缘
    pi = math.pi
    # 各点的信息
    for i in range(m):
        point[i] = tuple(map(int, input().split()))
        # 判断该点是否在黑洞边缘，即该点到中心的距离是否为r
        if sum([(point[i][j] - heidong[j])**2 for j in range(n)]) == r2:
            edge[i] = True

    dis = [[0] * m for _ in range(m)]
    # 构造点到点的距离矩阵,dis[i][j]表示点i到j的距离
    for i in range(m - 1):
        for j in range(i + 1, m):
            dis[i][j] = dis[j][i] = getdis(i, j)

    # print('打印距离')
    for i in range(m):
        print('%.14f' % (sum(dis[i])))  #14位小数
    # for tt in dis:
    #     print(tt)
    # print(dis)
