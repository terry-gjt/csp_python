# 小明放学 这个题确实有点难度
def st181202():
    r,y,g = list(map(int, input().split()))
    sum=0
    n=int(input())
    for i in range(0,n):
        a,b = list(map(int, input().split()))
        temp = sum % (r + g + y)
        if a==0:#0代表是道路，所需时间不会变
            sum+=b
        elif a==1:#1代表出发时是红灯，需计算到达时的灯的颜色和通过需要的时间
            # rrrrbrrrrgggggggggggggyyyyyyyyyyyrrrrrrrrrbrrrrrrggggggg
            if temp>b+g:#黄灯或下轮红灯
                waittime = b + g + y +r - temp
                sum += waittime
            elif temp<b:#红灯
                waittime=b-temp
                sum += waittime
        elif a==2:#2代表出发时是黄灯，需计算到达时的灯的颜色和通过需要的时间
            # yyyyyyyybyyyyyrrrrrrrrrrggggggggggggggyyyyyyyyybyyyyrrrrrrrrggggggggggg
            if temp > b + r+g:  # 下轮黄灯
                waittime = b + r+g + y + r - temp
                sum += waittime
            elif temp < b+r:  # 红灯
                waittime = b + r  - temp
                sum += waittime
        elif a==3:#3代表出发时是绿灯，需计算到达时的灯的颜色和通过需要的时间
            #ggggggbggggyyyyyyyyyyyrrrrrrrrrrrrggggggggbgggggg
            if temp > b and temp <b+y+r:  # 中间这段
                waittime = b+ y + r - temp
                sum += waittime
    print(sum)
if __name__ == '__main__':
    st181202()