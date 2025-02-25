import sys
from prac import dijkstra, delay_time, fibo, fibo_dp, cal_seat

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


# 네트워크 딜레이 타임 문제

assert delay_time([[2,1,1],[2,3,1],[3,4,1]], 4, 2) == 2
assert delay_time([[1,2,1]], 2, 1) == 1
assert delay_time([[1,2,1]], 2, 2) == -1


# 피보나치 수열 일반 계산 구현

assert fibo(10) == 55
assert fibo(100) == 354224848179261915075

# 피보나치 수열 DP 구현

assert fibo_dp(10) == 55
assert fibo_dp(100) == 354224848179261915075


# 극장 좌석 자리 구하기 문제

assert cal_seat(9,[4,7]) == 12
assert cal_seat(9,[2,4,7]) == 4
assert cal_seat(11,[2,5]) == 26
assert cal_seat(10,[2,6,9]) == 6