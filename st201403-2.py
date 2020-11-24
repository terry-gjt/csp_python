# 窗口
def st201403_2a():
    N,M = list(map(int, input().split()))
    windows = []
    attacks = []
    for i in range(0, N):
        windows.append(list(map(int, input().split())))
        windows[i].append(i+1)
    for i in range(0, M):
        attacks.append(list(map(int, input().split())))
    # windows = [[0, 0, 4, 4,1], [1, 1, 5, 5,2], [2, 2, 6, 6,3]]
    # attacks = [[1, 1], [0, 0], [4, 4], [0, 5]]
    for attack in attacks:
        x = attack[0]
        y = attack[1]
        # print('x', x, 'y', y)
        notprint=True
        for window in windows[::-1]:
            x1=window[0]
            y1=window[1]
            x2 = window[2]
            y2 = window[3]
            if(x1<=x and x<=x2 and y1<=y and y<=y2):
                windows.remove(window)
                windows.append(window)
                print(window[4])
                notprint=False
                break
        if(notprint):print('IGNORED')
def st201403_2():
    N, M = map(int, input().split())
    windows = []
    for i in range(N):
        p = list(map(int, input().split()))
        p.insert(0, i + 1)
        windows.append(p)
    for i in range(M):
        c = list(map(int, input().split()))
        for ind in range(N - 1, -1, -1):
            if windows[ind][1] <= c[0] <= windows[ind][3] and windows[ind][2] <= c[1] <= windows[ind][4]:
                print(windows[ind][0])
                a = windows.pop(ind)
                windows.append(a)
                break
        else:
            print('IGNORED')
if __name__ == '__main__':
    st201403_2()
