#报数
def fun(num):
    s_num=str(num)
    # print(s_num.count('7'))
    if(s_num.count('7')>0):return False #含有数字7
    elif (num % 7 == 0):return False    #能被7整除
    else:return True #返回真就报数

def st191201():
    n = int(input())
    times=[0,0,0,0]#跳过次数
    temp=0 #当前报数次数
    number=1 #下一个要报的数
    student=0 #下一个报数的人
    while(temp<n):
        if(fun(number)):
            # print('同学',student, '报数:',number)
            temp+=1
        else:
            times[student] = times[student] + 1
            # print('同学',student,'报数跳过')
        number+=1
        if(student==3):student=0
        else:student+=1
    print(times[0])
    print(times[1])
    print(times[2])
    print(times[3])


if __name__ == '__main__':
    st191201()