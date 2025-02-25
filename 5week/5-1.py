import heapq

def dijkstra(graph, start, end):
    # 거리 정보를 무한대로 초기화
    distances = {node:float('infinity') for node in range(1, len(graph) + 1)}
    distances[start] = 0 # 시작 노드 거리 = 0
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        # 현재 노드의 거리가 이미 알고 있는 거리보다 크면 무시
        if distances[current_node] < current_distance:
            continue

        for adj, weight in graph[current_node].items():
            distance = current_distance + weight

            # 인접 노드까지의 거리가 현재 알고 있는 거리보다 짧으면 업데이트
            if distance < distances[adj]:
                distances[adj] = distance
                heapq.heappush(queue, (distance, adj))

    return distances[end]

# 그래프를 인접 리스트로 표현
graph = {
    1:{2:4, 3:2},
    2:{1:4, 3:5, 4:1},
    3:{1:2, 2:5, 4:7},
    4:{2:1, 3:7}
}

A, B = 1, 4
print(dijkstra(graph, A, B))