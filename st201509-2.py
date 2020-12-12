# 日期计算
def st150902():
    year = int(input())
    day = int(input())
    days=[31,28,31,30,31,30,31,31,30,31,30,31]
    if year%4==0 and year%100!=0:
        days[1]=29
    elif year%400==0:
        days[1] = 29
    for month in range(12):
        if day>days[month]:
            day-=days[month]
        else:
            print(month+1)
            print(day)
            return
if __name__ == '__main__':
    st150902()