# 学生排队
def takeFirst(elem):
    return elem[0]
def takeSecond(elem):
    return elem[1]
def takeThird(elem):
    return elem[2]
def st170901():
    n=int(input())
    m = int(input())
    # n,m=8,3
    # s=['3 2',
    #    '8 -3',
    #    '3 -2']
    students=[]
    for j in range(1,n+1):
        students.append(j)
    for i in range(m):
        # student, move = list(map(int, s[i].split()))
        student,move= list(map(int, input().split()))
        index=students.index(student)
        if move>0:
            students.insert(index+move+1,student)
            students.remove(student)
        else:
            students.remove(student)
            students.insert(index + move, student)
        # print(students)
    for key in students:
        print(key,end=' ')

if __name__ == '__main__':
    st170901()