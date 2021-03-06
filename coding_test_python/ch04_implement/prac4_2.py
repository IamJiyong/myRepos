# 현민이는 게임 캐릭터가 맵 안에서 움직이는 시스템을 개발 중이다.
# 캐릭터가 있는 장소는 1x1 크기의 정사각형으로 이뤄진 NxM 크기의 직사각형으로, 각각의 칸은 육지 또는 바다이다.
# 캐릭터는 동서남북 중 한 곳을 바라본다.
# 맵의 각 칸은 (A, B)로 나타낼 수 있고, A는 북쪽으로부터 떨어진 칸의 개수, B는 서쪽으로부터 떨어진 칸의 개수이다.
# 캐릭터는 상하좌우로 움직일수 있고, 바다로 되어 있는 공간에는 갈 수 없다.
# 캐릭터의 움직임을 설정하기 위해 정해 놓은 메뉴얼은 이러하다.
# 1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 갈 곳을 정한다.
# 2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음 왼쪽으로 한 칸을 전진한다.
#    왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만 수행하고 1단계로 돌아간다.
# 3. 만약 네 방향 모두 이미 기본 칸이거나 바다로 되어 있는 칸인 경우에는,
#    바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다.
#    단, 이때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다.
# 메뉴얼에 따라 캐릭터를 이동시킨 뒤에, 캐릭터가 방문한 칸의 수를 출력하는 프로그램을 만드시오.

m, n = map(int, input().split())
y, x, d = map(int, input().split())

game_map = []
for i in range(m):
    game_map.append(list(map(int, input().split())))

next_move = [(0, -1), (1, 0), (0, 1), (-1, 0)]
back_move = [(-1, 0), (0, -1), (1, 0), (0, 1)]

game_map[y][x] = 2
result = 1

while True:
    moved = False

    for i in range(4): # 1,2단계. 왼쪽부터 4방향 순서대로 갈 수 있는지 확인
        d = (d + 3) % 4 # 왼쪽으로 회전
        dy, dx = y + next_move[d][0], x + next_move[d][1]
        if game_map[dy][dx] == 0: # 갈 수 있으면
            y, x = dy, dx
            game_map[y][x] = 2
            result += 1
            moved = True
            break

    if moved:
        continue
    
    dy, dx = y + back_move[d][0], x + back_move[d][1]
    if game_map[dy][dx] == 1:
        break
    else:
        y, x = dy, dx

print(result)