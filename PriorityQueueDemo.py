from queue import Queue,PriorityQueue

# 使用heapq实现优先队列
#定义一个可比较对象
class pqueue:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    #定义x为比较值，出队时输出x最小的，y为储存的其他值
    def __lt__(self, other):
        return self.x<other.x


def main():
    pq = PriorityQueue()
    print('0结束测试;1输入数字对;2输出优先队列队头')
    while 1:
        opt=int(input('请输入0-2: '))
        if opt==0:      #输入0，结束测试
            break
        elif opt==1:      #输入1，输入数字对
            x,y=map(int,input().split())
            pq.put(pqueue(x,y))    #插入数据
        elif opt==2:      #输入2，输出优先队列队头
            tmp=pq.get()
            print(tmp.x,tmp.y)    #提取队头
        else:
            print('输入有误')


if __name__=="__main__":
    main()
