# N x M 크기의 얼음 틀이 있다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다.
# 구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다.
# 이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하시오.
# 다음의 4 x 5 얼음 틀 예시에서는 아이스크림이 총 3개 생성된다.

def dfs(graph, m, n, v):

    graph[v[0]][v[1]] = 2
    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]

    for d in directions:
        dv = (v[0] + d[0], v[1] + d[1])
        if dv[0] >= 0 and dv[0] < m and dv[1] >= 0 and dv[1] < n:
            if graph[dv[0]][dv[1]] == '0':
                graph[dv[0]][dv[1]] = '2'
                dfs(graph, m, n, dv)

m, n = map(int, input().split())
map = []
for i in range(m):
    map.append(list(input()))

result = 0

for i in range(m):
    for j in range(n):
        if map[i][j] == '0':
            dfs(map, m, n, (i, j))
            result += 1

print(result)