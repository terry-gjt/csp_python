# 打酱油
def st170901():
    N = int(input())
    temp=0
    if N//50>0:
        temp+=N//50*7
        N=N%50
    if N//30>0:
        temp+=N//30*4
        N=N%30
    if N//10>0:
        temp+=N//10
        N=N%10
    # print(N)
    print(temp)
if __name__ == '__main__':
    st170901()