# 问题描述
# 二十四点
# 这个好像没成功
def st2():
    n = int(input())
    for i in range(n):
        a = input()
        b=[]
        c=[]
        before=0
        for i in a:
            if i in '+-*/':
                b.append(before)
                b.append(i)
                before=0
            elif i in '0123456789':
                before=before*10+int(i)
        else:b.append(before)
        print(b)
        for i in range(len(b)):
            if b[i] == '/':
                before=before//b[i+1]
            elif b[i] == '*':
                before = before * b[i + 1]
            elif b[i] == '+':
                c.append(before)
                c.append('+')
            elif b[i]== '-':
                c.append(before)
                c.append('-')
            else:
                before=b[i]
        else:c.append(before)
        print(c)
        for i in range(len(b)):
            if b[i] =='+':
                before = before + b[i + 1]
            elif b[i] == '-':
                before = before - b[i + 1]
            else:
                before=b[i]
        print(before)

#这个是另一种解法
def fun():
    n = int(input())
    result = []
    for i in range(n):
        temp = input()
        if 'x' in temp:
            temp = temp.replace('x', '*')
        if '/' in temp:
            temp = temp.replace('/', '//')
        if eval(temp) == 24:
            result.append('Yes')
        else:
            result.append('No')
    for i in result:
        print(i)

def st190302():
    n=int(input())
    for i in range(n):
        a = input().replace('/','//').replace('x', '*')
        num=eval(a)
        if num==24:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    # fun()
    # st2()
    st190302()

