# n = int(input())
# datas = []
# for i in range(n-1):
#     disList = list(map(int, input().split()))
#     datas.append(disList)

n = 3
datas = [[1, 2], [2, 3]]
# 弗洛伊德算法
def floyd():
    l = len(graph)
    for k in range(l):
        for i in range(l):
            for j in range(l):
                if k == i or k == j or i == j:
                    continue
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

# 构图
# graph = [[(lambda x: 0 if x[0] == x[1] else inf)([i, j]) for j in range(n)] for i in range(n)]
graph = [[float('inf') for j in range(n+1)] for i in range(n+1)]

for row in datas:
    graph[row[0]][row[1]] = 1
    graph[row[1]][row[0]] = 1

# print(graph)
floyd()
# print(graph)
dis0, dis1, dis2 = 0, 0, 0
for i in range(n+1):
    for j in range(i+1, n+1):
        if graph[i][j] % 3 == 0:
            dis0 += graph[i][j]
        if graph[i][j] % 3 == 1:
            dis1 += graph[i][j]
        if graph[i][j] % 3 == 2:
            dis2 += graph[i][j]

print(str(dis0) + ' ' + str(dis1) + ' ' + str(dis2))