import sys
from prac import dijkstra

with open('dijkstra_testcase.txt') as f:
    sys.stdin = f
    input = sys.stdin.readline
    n, m = map(int, input().split())
    start = int(input())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))

assert dijkstra(graph, start) == [1000000000, 0, 8, 9, 5, 7]