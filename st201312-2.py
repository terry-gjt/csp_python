# ISBN号码
def st201312_2():
    s = input()
    # s='0-670-82162-0'
    resultnum = 0
    i=1
    for strtemp in s[:-2]:
        if strtemp in '0123456789':
            resultnum+=int(strtemp)*i
            i+=1
    resultnum=resultnum%11
    if resultnum==10:
        resultnstr='X'
    else:
        resultnstr=str(resultnum)
    if resultnstr==s[-1]:
        print('Right')
    else:
        print(s[:-1],end='')
        print(resultnstr)

if __name__ == '__main__':
    st201312_2()