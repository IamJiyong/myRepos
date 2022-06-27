# 동빈이는 N x M 크기의 직사각형 형태의 미로에 갇혀 있다.
# 미로에는 여러 마리의 괴물이 있어 이를 피해 탈출해야 한다.
# 동빈이의 위치는 (1, 1)이고 미로의 출구는 (N, M)의 위치에 존재하며 한 번에 한 칸씩 이동할 수 있다.
# 이때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있다.
# 미로는 반드시 탈출할 수 있는 형태로 제시된다.
# 이때 동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하시오.
# 칸을 셀 대는 시작 칸과 마지막 칸을 모두 포함해서 계산한다.

from collections import deque

m, n = map(int, input().split())

graph = []
for i in range(m):
    graph.append(list(map(int, input())))

def print_graph(graph, m, n):
    for i in range(m):
        for j in range(n):
            print('%3d' % graph[i][j], end='')
        print()

def bfs(graph, m, n, start):
    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]

    queue = deque([start])
    # graph[start[0]][start[1]] = 2
    while queue:
        print()
        # print_graph(graph, m, n)
        v = queue.popleft()
        for d in directions:
            dv = (v[0] + d[0], v[1] + d[1])
            if dv[0] < 0 or dv[0] >= m or dv[1] < 0 or dv[1] >= n:
                continue
            if graph[dv[0]][dv[1]] == 1:
                graph[dv[0]][dv[1]] = graph[v[0]][v[1]] + 1
                queue.append(dv)

bfs(graph, m, n, (0, 0))
print(graph[m - 1][n - 1])