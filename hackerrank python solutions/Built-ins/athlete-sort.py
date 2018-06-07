N, M = map(int, input().split())
j = [[int(x) for x in input().split()] for i in range(N)]
k = int(input())
j.sort(key=lambda row: row[k])
for m in j:
    print(*m)