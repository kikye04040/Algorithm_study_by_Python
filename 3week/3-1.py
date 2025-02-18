from collections import deque

def bfs_maze_escape(maze):
    N, M = len(maze), len(maze[0]) # 미로의 크기
    visited = [[False] * M for _ in range(N)] # 방문한 위치를 추적하는 배열
    queue = deque([(0, 0, 1)]) # 큐 초기화: 시작 위치와 경로 길이 (x, y, distance)
    visited[0][0] = True # 시작 위치 방문 처리

    # 이동 가능한 방향: 상, 하, 좌, 우
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y, dist = queue.popleft()

        # 출구에 도달 시 현재 경로 길이 반환
        if x == N-1 and y == M-1:
            return dist

        # 모든 가능한 방향으로 이동
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # 이동 가능한 위치인지 확인하고, 아직 방문하지 않았다면 큐에 추가
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and maze[nx][ny] == "1":
                visited[nx][ny]== True
                queue.append((nx, ny, dist + 1))

    # 출구에 도달할 수 없는 경우
    return -1

# 예시 입력
maze = [
    "11101",
    "10101",
    "10101",
    "11111"
]

# 문자열을 리스트로 변환하여 입력
maze = [list(row) for row in maze]

# 함수 실행 및 결과 출력
print(bfs_maze_escape(maze))