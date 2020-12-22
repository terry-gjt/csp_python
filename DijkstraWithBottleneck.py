# we define the length of a path to be the sum of the lengths of its edges.
# Define the bottleneck of a path to be the maximum length of one of its edges.
# A mininum-bottleneck path between two vertices s and t is a path with bottleneck no larger than that of any other s-t path.
# Show how to modify Dijkstra's algorithm tocompute a minimum-bottleneck path between two given vertices.
# The running timeshould be O(mlogn), as in lecture.
# 最小瓶颈路径（路径的最大边相比其他路径最小）
# 我们把一条路的长度定义为它的长度之和边缘。定义一条路径的瓶颈是它的一条边的最大长度。
# 顶点s和t之间的最小瓶颈路径是一条瓶颈不大于任何其它s-t路径的路径。演示如何修改Dijkstra的算法来计算两个给定顶点之间的最小瓶颈路径。
# 运行时间应该是O（mlogn）。

#dijkstra原算法参考自https://blog.csdn.net/weixin_39433783/article/details/82954269
graph = {}
graph["start"] = {}
graph["start"]["a"] = 10
graph["start"]["b"] = 6
graph["start"]["end"] = 17

graph["a"] = {}
graph["a"]["end"] = 9
graph["a"]["c"] = 9
graph["a"]["start"] = 10

graph["b"] = {}
graph["b"]["c"] = 5
graph["b"]["6"] = 9

graph["c"] = {}
graph["c"]["d"] = 4
graph["c"]["f"] = 7
graph["c"]["a"] = 9
graph["c"]["b"] = 5

graph["d"] = {}
graph["d"]["e"] = 6
graph["d"]["c"] = 4

graph["e"] = {}
graph["e"]["d"] = 6

graph["f"] = {}
graph["f"]["g"] = 8
graph["f"]["c"] = 7

graph["g"] = {}
graph["g"]["end"] = 4
graph["g"]["f"] = 8

graph["end"] = {}
graph["end"]["g"] = 4
graph["end"]["a"] = 9
graph["end"]["start"] = 17

# 无穷大
infinity = float("inf")
costs = {}

# 父节点散列表
parents = {}

# 已经处理过的节点，需要记录
processed = []

def addcosts(node):
    for cost in graph[node]:
        costs[cost]=graph[node][cost]
# 找到开销最小的节点
def find_lowest_cost_node(costs):
    # 初始化数据
    lowest_cost = infinity
    lowest_cost_node = None
    # 遍历所有节点
    for node in costs:
        # 该节点没有被处理
        if not node in processed:
            # 如果当前节点的开销比已经存在的开销小，则更新该节点为开销最小的节点
            if costs[node] < lowest_cost:
                lowest_cost = costs[node]
                lowest_cost_node = node
    return lowest_cost_node


# 找到最短路径
def find_shortest_path():
    node = "end"
    shortest_path = ["end"]
    while parents[node] != "start":
        shortest_path.append(parents[node])
        node = parents[node]
    shortest_path.append("start")
    return shortest_path


# 寻找加权的最短路径
def dijkstra():
    # 查询到目前开销最小的节点
    node = find_lowest_cost_node(costs)
    # 只要有开销最小的节点就循环（这个while循环在所有节点都被处理过后结束）
    while node is not None:
        # 获取该节点当前开销
        cost = costs[node]
        # 获取该节点相邻的节点
        neighbors = graph[node]
        # 遍历当前节点的所有邻居
        for n in neighbors.keys():
            # 计算经过当前节点到达相邻结点的开销,即当前节点的开销加上当前节点到相邻节点的开销
            new_cost = cost + neighbors[n]
            # 如果经当前节点前往该邻居更近，就更新该邻居的开销
            if new_cost < costs[n]:
                costs[n] = new_cost
                #同时将该邻居的父节点设置为当前节点
                parents[n] = node
        # 将当前节点标记为处理过
        processed.append(node)
        # 找出接下来要处理的节点，并循环
        node = find_lowest_cost_node(costs)
    # 循环完毕说明所有节点都已经处理完毕
    shortest_path = find_shortest_path()
    shortest_path.reverse()
    print(shortest_path)
# 测试
dijkstra()

